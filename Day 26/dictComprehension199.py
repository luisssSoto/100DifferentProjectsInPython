"""Dictionary Comprehension"""
from random import randrange
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_score = {name:randrange(1, 101) for name in names}
print(students_score)

# Challenge 1:
passed_students = {student:score for (student, score) in students_score.items() if score >= 60}
print(passed_students)