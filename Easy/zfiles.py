# create_py_files.py

for i in range(1, 11):
    filename = f"practice21/04/25{i}.py"
    with open(filename, "w") as f:
        f.write(f"# This is {filename}\n\n")
        

print("Python files created successfully!")
