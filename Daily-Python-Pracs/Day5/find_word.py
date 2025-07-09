def count_word_lines(filepath: str, word: str) -> tuple[int, list[int]]:

    """count lines where a specific word exists and return it with its lines nums"""

    if not word:
        return 0, []
    
    word = word.lower()
    count = 0
    line_numbers = []

    try:
        with open(filepath, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if word in line.lower():
                    count += 1
                    line_numbers.append(line_num)

        return count, line_numbers
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return 0, []
    

if __name__ == "__main__":

    result = count_word_lines("sample.txt", "test")
    print(f"Count: {result[0]}, Lines: {result[1]}")