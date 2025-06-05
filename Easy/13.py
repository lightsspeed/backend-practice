import random

def random_integers(n: int, min_val: int, max_val: int) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(n)]

# Test cases
if __name__ == "__main__":
    random.seed(42)  # Set seed for reproducibility
    print(random_integers(5, 1, 10))  # Example output: [6, 3, 7, 4, 6]
    print(random_integers(3, 0, 5))   # Example output: [2, 1, 5]
    print(random_integers(0, 1, 10))  # Output: []



# def count_vowels(text: str) -> int:
    # return sum(1 for char in text.lower() if char in {'a', 'e', 'i', 'o', 'u'})