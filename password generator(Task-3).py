import random
import string

def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
