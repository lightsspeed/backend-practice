# This is 4.py

# Create a program to implement a simple LRU (Least Recently Used) Cache with a capacity of 2.


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Dictionary for O(1) access
        self.order = []  # List to track order of use
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) >= self.capacity:
            lru_key = self.order.pop(0)
            del self.cache[lru_key]
        self.cache[key] = value
        self.order.append(key)
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # Output: 1
cache.put(3, 3)  # Evicts key 2
print(cache.get(2))  # Output: -1