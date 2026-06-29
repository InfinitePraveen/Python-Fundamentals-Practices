# Ask user to create a password
# Password must:
# - Be at least 8 characters long
# - Contain at least one uppercase letter
# - Contain at least one lowercase letter
# - Contain at least one digit

while True:
    password = input("Create a password: ")

    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue

    # Check for lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        continue

    # Check for digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        continue

    # If all checks pass, exit the loop
    print("Password successfully created!")
    break

# Keep asking until they enter a valid password
# Use a while loop