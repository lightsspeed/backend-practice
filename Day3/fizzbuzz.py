def fizzbuzz() -> list[str]: #to return the o/p in list
    result = [] # storing the result
    for num in range(1, 16):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        
        elif num % 3 == 0:
            result.append("Fizz")
        
        elif num % 5 == 0:
            result.append("Buzz")

        else:
            result.append(str(num))
    return result


if __name__ == "__main__":

    print(fizzbuzz())