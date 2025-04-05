# create_py_files.py

for i in range(11, 21):
    filename = f"{i}.py"
    with open(filename, "w") as f:
        f.write(f"# This is {filename}\n\n")
        

print("Python files created successfully!")
