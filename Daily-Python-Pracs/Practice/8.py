
# Count Multiples of 7 (1 to 100)Write a Python program to count how many numbers between 1 and 100 are divisible by 7.Expected Output: 14Tests: Loops, conditionals, counter variable.☺


count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1

print("Count of numbers between 1 and 100 that are divisible by 7:", count)

