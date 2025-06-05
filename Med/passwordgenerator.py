#password generator.py
import random

import string

def generate_password(length=12, use_special_chars=True):

    """Generate a random password.

    Args:
        length (int): Length of the password. Default is 12.
        use_special_chars (bool): Whether to include special characters. Default is True.

    Returns:
        str: Generated password.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ""

    # Ensure the password contains at least one character from each set
    password_characters = (
        random.choice(lowercase) +
        random.choice(uppercase) +
        random.choice(digits) +
        random.choice(special_chars)
    )

    # Fill the rest of the password length with random choices from all sets
    all_characters = lowercase + uppercase + digits + special_chars
    password_characters += ''.join(random.choice(all_characters) for _ in range(length - len(password_characters)))

    # Shuffle the characters to ensure randomness
    password = ''.join(random.sample(password_characters, len(password_characters)))

    return password 

print(generate_password(8, True))  # Example usage
#print(generate_password(16, False))  # Example usage without special characters