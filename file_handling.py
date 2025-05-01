# File Handling
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")  # Writes to a file

with open("sample.txt", "r") as file:
    content = file.read()  # Reads the file
    print(content)