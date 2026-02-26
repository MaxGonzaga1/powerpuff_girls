#Creating a password validator that checks for the following criteria:
#1. The password must contain at least one letter.
#2. The password must contain at least one digit.
#3. The password must contain at least one special character (e.g., !, @, #, $, etc.).
#4. The password must be at least 8 characters long.

import string

while True:
    fromUser = input("Set your password: ")
    
    hasLetter = False
    hasDigit = False
    hasSpecial = False
    
    for char in fromUser:
        if char.isalpha():
            hasLetter = True
        elif char.isdigit():
            hasDigit = True
        elif char in string.punctuation:
            hasSpecial = True
    
    if not hasLetter:
        print("Password must contain at least one letter.")
    elif not hasDigit:
        print("Password must contain at least one digit.")
    elif not hasSpecial:
        print("Password must contain at least one special character.")
    elif len(fromUser) < 8:
        print("Password must be at least 8 characters long.")
    else:
        print("Password accepted.")
        break