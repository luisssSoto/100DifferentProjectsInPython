"""Raising Our Own Exceptions"""

height = float(input("Height: "))
weight = int(input("Weight: "))

class HumanHeightError(ValueError):
    def __init__(self, error_message):
        super().__init__(error_message)

if height >= 3:
    raise HumanHeightError("Human Height is lesser than 3 meters")

bmi = weight / height ** 2
print(bmi)