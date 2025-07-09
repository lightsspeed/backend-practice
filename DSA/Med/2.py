# This is 2.py

# Create a program to reverse a string (e.g., "python") without using built-in methods.

text = "Python"
reversed_text = ""  


for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
print(reversed_text)  # Output: "nohtyP"