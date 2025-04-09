# This is Slice5.py

# In a scenario, create a generator that yields combinations of two numbers from [1, 2, 3] without repetition.

def combination_generator(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            yield (numbers[i], numbers[j])
for comb in combination_generator([1, 2, 3]):
    print(comb)  # Output: (1, 2), (1, 3), (2, 3)