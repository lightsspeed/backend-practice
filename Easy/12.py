# Question: Write a Python function that counts the number of vowels (a, e, i, o, u) in a given string, ignoring case. Example: "Hello" → 2.

def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Test cases
if __name__ == "__main__":
    print(count_vowels("Hello"))      # Output: 2
    print(count_vowels("PYTHON"))     # Output: 1
    print(count_vowels(""))           # Output: 0
