def greater(numbers: list[float]) -> list[float]:

    return sorted(list(filter(lambda x:x > 10, numbers)))
    


if __name__ == "__main__":

    numbers = [1,23,2,5,15,22,8,45]

    print((greater(numbers)))