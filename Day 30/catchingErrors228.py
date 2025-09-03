"""Catching Errors """

try:
    file = open("passwordManager2/data.txt", "r")
    d = {"key":"value"}
    print(d["key"])
except FileNotFoundError:
    file = open("passwordManager2/data.txt", "w")
    file.write("Something")
except KeyError as error:
    print(f"Error: {error} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")