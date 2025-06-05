def print_long_lines(file_path: str) -> None:
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove trailing newline for length check
                line = line.rstrip('\n')
                if len(line) > 10:
                    print(line)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error: Could not read file '{file_path}': {e}")

# Test case
if __name__ == "__main__":
    print_long_lines("input.txt")