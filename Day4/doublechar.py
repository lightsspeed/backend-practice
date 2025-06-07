def doublechar(text: str) -> str:

    # return [char * 2 for char in text]
    return "".join(char * 2 for char in text)


if __name__ == "__main__":

    print(doublechar("Akhi"))