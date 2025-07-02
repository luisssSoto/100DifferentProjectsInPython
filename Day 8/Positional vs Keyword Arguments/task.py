# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# 1.
def greet_with(name, location):
    print(f"My name is: {name} and my location is: {location}")

greet_with('Alex', 'Texas')

# 2.
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# 3. Keyword arguments
greet_with(location='Zapopan', name='Jacinto')
print('ALEX'.lower())