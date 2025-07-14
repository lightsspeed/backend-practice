def increment_nums(nums: list[float]) -> list[float]:

    return [num + 1 for num in nums]

if __name__ == "__main__":

    print(increment_nums([1,2,3]))