# Question: Write a Python function that takes a list as input and returns a new list with the elements in reverse order. Example: [1, 2, 3, 4] → [4, 3, 2, 1].


def reverse_list(input_list):

    input_list = input_list[::-1]
    return input_list

# Example usage
if __name__ == "__main__":
    example_list = [1, 2, 3, 4]
    reversed_list = reverse_list(example_list)
    print(reversed_list)  # Output: [4, 3, 2, 1]