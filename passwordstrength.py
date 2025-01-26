import re

def check_password_strength(password):
    if len(password) < 8:
        return "Your Password is too short. It should be at least 8 characters."
    if not re.search("[a-z]", password):
        return "Your Password should contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Your Password should contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return " Your Password should contain at least one digit."
    if not re.search("[!@#$%^&*()_+]", password):
        return " Your Password should contain at least one special character."
    return " Your Password is strong!"

# Test the function
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))

