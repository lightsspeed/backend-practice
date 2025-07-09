# This is 4.py

# Find the index of the first occurrence of an item (e.g., 3) in a list.



def find_index(list, target):

    for i in range(len(list)):
        if list[i] == target:
            return i
    
    return -1 


if __name__ == "__main__":

    num = [1, 2, 3, 4]

    target = 3

    result = find_index(num, target)
    
    print(f"The index of {target} is {result}")
        
