#Q1. Write a Python program to perform the following: 
#Validate a given public IP address to check if it follows the correct format (IPv4).
#Validate a given email address to check if it’s a valid Gmail address, considering:
#It should contain "@gmail.com".
#The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
#Provide informative error messages for invalid IP or email.



import re
import ipaddress

def check_ip(ip):
    rule = r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$"
    if not re.match(rule, ip):
        return "galat IP hai bhai"
    

    ipadd_obj= ipaddress.ip_address(ip)
    return "Private hai" if ipadd_obj.is_private else "Public hai"

def check_email(email):
   rule = r"^[a-z0-9._%+-]+@gmail\.com$"
   rule= r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
   return "sahi hai" if re.match(rule, email) else "galat mail id"

def main():
    ip = input("IP type kijye: ")
    print(check_ip(ip))
    
    email = input("Email type kijye: ")
    print(check_email(email))

main()