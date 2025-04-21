# Sum of Multiples of 3 (1 to 100)Write a Python program to calculate the sum of all numbers divisible by 3 from 1 to 100.Expected Output: 1683Tests: Loops, conditionals (using modulo), accumulation.


sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        sum += i
print("Sum of multiples of 3 from 1 to 100 is:", sum)
    