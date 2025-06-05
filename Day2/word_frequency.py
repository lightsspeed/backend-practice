
import string

def word_frequency(sentence: str) -> dict[str, int]:
    # Remove punctuation and convert to lowercase
    sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    # Split into words and filter out empty strings
    words = [word for word in sentence.split() if word]
    # Count frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Test cases
if __name__ == "__main__":
    print(word_frequency("The quick brown fox jumps. The fox runs."))  
    # Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'runs': 1}
    print(word_frequency("Hello, hello!"))  # Output: {'hello': 2}
    print(word_frequency(""))  # Output: {}
    print(word_frequency("!@#$"))  # Output: {}
