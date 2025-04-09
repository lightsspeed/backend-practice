# This is Slice1.py

# You’re debugging a generator def gen(): yield x that raises an UnboundLocalError with x = 5. Explain the issue and fix it.


def gen():
    x = 5  # Define x before yield
    yield x
for val in gen():
    print(val)  # Output: 5