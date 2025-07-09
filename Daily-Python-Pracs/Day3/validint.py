
def get_valid_integer() -> int:
    while True:
        try:
            user_input = input("Enter an integer: ")
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Test case
if __name__ == "__main__":
    number = get_valid_integer()
    print(f"You entered: {number}")
