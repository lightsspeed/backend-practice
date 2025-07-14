def factorial(n: int) -> int:
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Test cases
if __name__ == "__main__":
    try:
        print(factorial(5))  # Output: 120
        print(factorial(0))  # Output: 1
        print(factorial(3))  # Output: 6
        # print(factorial(-1))  # Raises ValueError
        # print(factorial(1.5))  # Raises TypeError
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")