# This is 7.py
# Write a generator function that yields the uppercase version of each word in a sentence 'python is fun'.


def upper_word_generator(text):
    for word in text.split():
        yield word.upper()
for word in upper_word_generator('python is fun'):
    print(word)  # Output: PYTHON, IS, FUN