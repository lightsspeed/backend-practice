# Count Odd Numbers (1 to 50)Write a Python program to count how many odd numbers are between 1 and 50 (inclusive).Expected Output: 25Tests: Loops, conditionals, counter variable.☺


count = 0
for i in range(1, 51):
    if i % 2 != 0:
        count += 1
print("Count of odd numbers between 1 and 50:", count)