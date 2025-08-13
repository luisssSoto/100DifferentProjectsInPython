"""Absolute and Relative Path"""

# Relative Path
with open("../../../../Desktop/new_file.txt", "w") as new_file:
    new_file.write("Waves from desktop")

with open("../../../../Desktop/new_file.txt", "r") as new_file:
    print(new_file.read())

# Absolute Path
with open("C:\\Users\\aleja\\Desktop\\new_file.txt", "r") as new_file:
    print(new_file.read())