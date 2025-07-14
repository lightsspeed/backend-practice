from typing import Tuple



def longest_word(text: str, len: int) -> Tuple[str , int]:

    words = text.split()
    return max(words , key=len, default="")


if __name__ == "__main__":
    print(longest_word("Akhilesh is practicing python"))
    print(longest_word("Akhi is devops engineer"))
    print(longest_word("AC is a Human"))