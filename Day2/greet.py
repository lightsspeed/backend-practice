
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# Test cases
if __name__ == "__main__":
    print(greet("John"))            # Output: Hello, John!
    print(greet("Alice", "Hi"))     # Output: Hi, Alice!
    print(greet("", "Welcome"))     # Output: Welcome, !
    print(greet("Bob", ""))         # Output: , Bob!
