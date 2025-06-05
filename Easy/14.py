import random

def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def random_integers(n: int, min_val: int, max_val: int) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(n)]

# Test cases
if __name__ == "__main__":
    # random.seed(42)  # Set seed for reproducibility
    numbers = random_integers(10, 1, 50)  # Generate list: [6, 3, 7, 4, 6]
    print(numbers)  # Output: [6, 3, 7, 4, 6]
    print(sum_even_numbers(numbers))  # Output: 16 (sum of 6, 4, 6)

