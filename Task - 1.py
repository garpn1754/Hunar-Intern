def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(not char.isalnum() for char in password):
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Okay"
    else:
        return "Weak"

password = input("Enter a password: ")
print("Password strength:", check_password_strength(password))
