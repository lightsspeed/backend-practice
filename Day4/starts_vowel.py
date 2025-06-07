def starts_vowel(text : str) -> bool:

    if not text:
        return False
    return text[0].lower() in {'a', 'e', 'i', 'o', 'u'}

if __name__ == "__main__":

    print(starts_vowel("apple"))