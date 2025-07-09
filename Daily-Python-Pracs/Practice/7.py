# Sum of Digits in 12345Write a Python program to find the sum of all digits in the number 12345.Expected Output: 15Tests: Loops, division, modulo, handling integers.☺
number = 12345
sum_of_digits = 0

while number > 0:
    digit = number % 10  # Get the last digit
    print("Current digit:", digit)  # Print current digit for debugging
    
    sum_of_digits += digit  # Add it to the sum
    print("Current sum:", sum_of_digits)  # Print current sum for debugging
    
    number //= 10  # Remove the last digit
    print("Remaining number:", number)  # Print remaining number for debugging


print("Sum of digits in 12345 is:", sum_of_digits)