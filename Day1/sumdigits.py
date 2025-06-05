def sum_digits(num: int) -> int:
    return sum(int(digit) for digit in str(num))

if __name__ == "__main__":

    print(sum_digits(123))
    print(sum_digits(111))
    print(sum_digits(1212512532))
    print(sum_digits(67345))