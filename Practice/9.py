# Sum of Alternating Numbers (1 to 10)Write a Python program to compute the sum of numbers from 1 to 10 with alternating signs (e.g., 1 - 2 + 3 - 4 + ... + 10).Expected Output: 5Tests: Loops, conditionals, alternating operations.☺

#
sum_of_alternating_numbers = 0

for i in range(1, 11):
    if i % 2 == 0:
        sum_of_alternating_numbers -= i
    else:
        sum_of_alternating_numbers += i

print("Sum of alternating numbers from 1 to 10 is:", sum_of_alternating_numbers)