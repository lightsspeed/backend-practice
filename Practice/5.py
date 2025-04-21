# Sum of Numbers Divisible by 5 (1 to 100)Write a Python program to calculate the sum of all numbers divisible by 5 from 1 to 100.Expected Output: 1050Tests: Loops, modulo operator, accumulation.☺


sum_of_numbers = 0
for i in range(1, 101):
    if i % 5 == 0:
        sum_of_numbers += i

print("Sum of numbers divisible by 5 from 1 to 100 is:", sum_of_numbers)