#Q2. Write a Python program that generates a password with the following conditions:
#At least one uppercase letter.
#At least one lowercase letter.
#At least two numbers.
#At least one special character (e.g., !@#$%&*).
#The password should be exactly 16 characters long.
#The password should contain no repeating characters.
#The password should have a random order each time.


import random
import string

import random
import string

def generate_password():
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    
    numbers = random.sample(string.digits, 2)
    
    special_character = random.choice("!@#$%&*")
    
    password_chars = []
    password_chars.append(uppercase_letter)
    password_chars.append(lowercase_letter)
    password_chars.extend(numbers)
    password_chars.append(special_character)
    
    additional_chars = random.sample(string.ascii_letters + string.digits + "!@#$%&*", 11)
    password_chars.extend(additional_chars)
    
    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    
    return password

print(generate_password())
