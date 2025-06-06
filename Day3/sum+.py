

def sum_positives(lst: list) -> int:

    return sum(num for num in lst if num > 0)


if __name__ == "__main__":

    print(sum_positives([1,-2,3,-4,4.4]))