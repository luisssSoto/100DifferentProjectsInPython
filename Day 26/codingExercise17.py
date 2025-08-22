with open("file1.txt", "r") as file1:
    lines = file1.readlines()
file1_list = [int(n.strip()) for n in lines]

with open("file2.txt", "r") as file2:
    lines = file2.readlines()
file2_list = [int(n.strip()) for n in lines]


result = [n for n in file1_list if n in file2_list]

print(result)