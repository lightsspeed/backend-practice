def get_digits(text: str ) -> list[str]:

    return [char for char in text if char.isdigit()]


if __name__ == "__main__":

    print(get_digits("hello123231123"))