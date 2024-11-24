import os
import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define the character pool: letters, digits, and punctuation
    character_pool = string.ascii_letters + string.digits + string.punctuation
    
    # Use os.urandom to genrate the password 
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
