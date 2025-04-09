# This is 4.py
# How can you use a generator to read a large file line by line without loading it all into memory?

def read_file_lines(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()
for line in read_file_lines('data.txt'):
    print(line)  # Yields each line