import random

def randomness(n: int , min: int, max:int) -> list[int]:
    return [random.randint(min, max) for _ in range(n)] 


def max(numbers: int) -> int:

    if not numbers:
        return None
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
    

if __name__ == "__main__":

    numbers = randomness(5, 1 , 20)
    print(numbers)
    print(max(numbers))


