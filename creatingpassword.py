import re
import getpass

def generate_password(password):
    errors = []

    # Minimum length
    if len(password) < 8:
        errors.append("Password must be at least 10 characters long")

    # Uppercase
    if not re.search(r"[A-Z]", password):
        errors.append("Must contain at least one uppercase letter")

    # Lowercase
    if not re.search(r"[a-z]", password):
        errors.append("Must contain at least one lowercase letter")

    # Digit
    if not re.search(r"[0-9]", password):
        errors.append("Must contain at least one number")

    # Special character
    if not re.search(r"[!@#$%^&*]", password):
        errors.append("Must contain at least one special character (!@#$%^&*)")

    # Email-style check (something@something)
    #if not re.match(r"^[A-Za-z0-9]+@[A-Za-z0-9]+[!@#$%^&*]$", password):
        #errors.append("Must follow email-style format like Name123@Domain9#")
    
    return errors


while True:

    print("\nCreate a strong password (Example: Ankitsavita@123)")
    user_password =getpass.getpass("enter your passwrod:")
    validation_errors = generate_password(user_password)

    if not validation_errors:
        print("Password created successfully.")
        break
    else:
        print("Password is not valid!")
        for errors in validation_errors:
            print("-",errors)
        print("Please try again.")