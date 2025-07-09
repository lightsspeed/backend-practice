# This is 3.py

# Write a generator function that yields prime numbers up to 20.

def prime_generator():
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False
        return True
    for i in range(2, 21):
        if is_prime(i):
            yield i
for p in prime_generator():
    print(p)  # Output: 2, 3, 5, 7, 11, 13, 17, 19