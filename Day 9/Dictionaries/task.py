programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retrieve values
print(programming_dictionary["Bug"])

# Create an empty dictionary
new_dictionary = {}
print(type(new_dictionary))

# Add items
programming_dictionary["Error"] = "A human error which can cause a bug in the program (typos) for instance"
print(programming_dictionary["Error"])

# Edit Values
programming_dictionary["Error"] = "Give up"
print(programming_dictionary["Error"])

# Print the keys
for key in programming_dictionary:
    print(key, end=' | ')
print()

# Print the values
for key in programming_dictionary:
    print(programming_dictionary[key], end=' | ')
print()