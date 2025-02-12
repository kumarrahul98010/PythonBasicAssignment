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
   return "sahi hai" if re.match(rule, email) else "galat mail id"

def main():
    ip = input("IP type kijye: ")
    print(check_ip(ip))
    
    email = input("Email type kijye: ")
    print(check_email(email))

main()