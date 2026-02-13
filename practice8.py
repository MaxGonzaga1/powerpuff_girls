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