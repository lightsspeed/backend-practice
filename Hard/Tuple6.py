# This is Tuple6.py

# Implement a function to detect a cycle in a tuple (simulating a linked list).

def has_cycle(tup):
    slow = fast = 0
    while fast < len(tup) and fast + 1 < len(tup):
        slow = tup[slow]
        fast = tup[tup[fast]]
        if slow == fast:
            return True
    return False
print(has_cycle((1, 2, 3, 1)))  # Output: True