# This is 8.py
# Use a while loop to remove items from a list until it’s empty.

def empty_list(my_list):
    while my_list:
        item = my_list.pop(0)  # remove the first element
        print(f"Removed: {item} | Remaining: {my_list}")
    print("The list is now empty.")

# Example usage:
my_items = ['apple', 'banana', 'cherry', 'date']
empty_list(my_items)
