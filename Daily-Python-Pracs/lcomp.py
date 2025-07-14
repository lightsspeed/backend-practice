def squares() -> int:
    return [num*num for num in range(1,21) if num % 2 == 0 ]


if __name__ == "__main__":

    print(squares())