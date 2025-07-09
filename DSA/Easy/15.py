def check_palindrome(text: str) -> bool:
    text.lower()
    return text == text[::-1]


if __name__ == "__main__":
    print(check_palindrome("hello"))
    print(check_palindrome("anu"))
    print(check_palindrome("anagram"))
    print(check_palindrome("nitin"))
    print(check_palindrome("race"))
