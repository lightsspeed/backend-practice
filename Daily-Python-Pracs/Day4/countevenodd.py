def count_even_odd(nums: list[int]) -> tuple[int, int]:
    even = sum(1 for num in nums if num % 2 == 0)
    odd = len(nums) - even
    return even, odd

if __name__ == "__main__":

    print(count_even_odd([1,3,5,21,6,-2]))