# Use an if-else statement to check if a variable (e.g., 7) is greater than 5.


number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    if number > 5:
        print(f"{number} is greater than 5.")
    else:
        print(f"{number} is not greater than 5.")


# Output: "7 is greater than 5."
# Output: "3 is not greater than 5."    
print("Please enter a valid number.")