# This is 6.py


# Create a program to rotate a list by 1 position to the right.


def rotate_right_by_one(list):
    if not list:
        return list  # Return empty list if input is empty
    
    # Save the last element
    last_element = list[-1]
    
    # Shift elements to the right
    for i in range(len(list) - 1, 0, -1):
        list[i] = list[i - 1]
    
    # Place the last element at the beginning
    list[0] = last_element
    
    return list

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    rotated_list = rotate_right_by_one(my_list)
    print(f"Original list: [1, 2, 3, 4, 5]")
    print(f"Rotated list: {rotated_list}")



# # #  ## Starting with list = [1, 2, 3, 4, 5]
# # for i in range(len(list) - 1, 0, -1): -> for i in range(4, 0, -1):
# # This means i will take values: 4, 3, 2, 1
# Now let's trace through each iteration:
# When i = 4:
# lst[4] = lst[4 - 1]  # lst[4] = lst[3]
# # lst becomes [1, 2, 3, 4, 4]
# When i = 3:
# lst[3] = lst[3 - 1]  # lst[3] = lst[2]
# # lst becomes [1, 2, 3, 3, 4]
# When i = 2:
# lst[2] = lst[2 - 1]  # lst[2] = lst[1]
# # lst becomes [1, 2, 2, 3, 4]
# When i = 1:
# lst[1] = lst[1 - 1]  # lst[1] = lst[0]
# # lst becomes [1, 1, 2, 3, 4]
# After the loop, we set:
# Lst[0] = last_element  # lst[0] = 5
# # lst becomes [5, 1, 2, 3, 4]
#         
    
#     # Place the last element at the beginning
#     list[0] = last_element