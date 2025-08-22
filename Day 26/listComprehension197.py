"""List Comprehension"""
# Challenge 1
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers] # new_list = [new_item for item in list]
print(new_numbers)

# Challenge 2
name = "Luis"
new_list = [letter for letter in name]
print(new_list)

# Challenge 3
double_num = [num * 2 for num in range(1, 5)]
print(double_num)

# Challenge 4: Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)
