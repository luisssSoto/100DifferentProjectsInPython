"""Open, Read, and Write a File"""

with open("new_file.txt", "w") as new_file:
    new_file.write("This is a brand new file")

with open("new_file.txt", "r") as new_file:
    content = new_file.read()
    print(content)

with open("new_file.txt", "a") as new_file:
    new_file.write("\nBy Alex Soto")

with open("new_file.txt", "r") as new_file:
    content = new_file.read()
    print(content)

with open("new_file.txt", "w") as new_file:
    new_file.write("Replace the whole content")

with open("new_file.txt", "r") as new_file:
    content = new_file.read()
    print(content)