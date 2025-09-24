"""Type Hints and Arrows"""

def is_valid_age(age: int)->bool:
    if age < 18:
        return False
    else:
        return True