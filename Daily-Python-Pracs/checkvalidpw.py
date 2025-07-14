
def validate_password() -> bool:
    """Prompt user for a password and validate it with multiple attempts.

    Criteria:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character from !@#$%^&*

    Returns:
        True if a valid password is entered, False if user exits with empty input
    """
    special_chars = "!@#$%^&*"
    
    while True:
        password = input("Enter a password (or press Enter to exit): ").strip()
        if not password:  # Exit on empty input
            print("Exiting without a valid password.")
            return False
        
        # Check length
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        
        # Initialize flags for each criterion
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        # Check each character
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True
        
        # Provide specific feedback if invalid
        if not has_upper:
            print("Password must contain at least one uppercase letter.")
            continue
        if not has_lower:
            print("Password must contain at least one lowercase letter.")
            continue
        if not has_digit:
            print("Password must contain at least one digit.")
            continue
        if not has_special:
            print("Password must contain at least one special character from !@#$%^&*.")
            continue
        
        # All criteria met
        print("Valid password!")
        return True

# Test the function
if __name__ == "__main__":
    validate_password()
