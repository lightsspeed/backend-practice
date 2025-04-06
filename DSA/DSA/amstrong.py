# Define the number of rows for the equilateral triangle
rows = 5

# Loop through each row
for i in range(1, rows + 1):
    # Print spaces to center the asterisks
    print(" " * (rows - i), end="")
    # Print asterisks with spaces in between
    print("* " * i)
