"""Iterate Pandas Frame"""
import random
students_name = ["Naruto", "Sasuke", "Sakura", "Hinata"]
score_students = [random.randint(1, 100) for x in range(len(students_name))]
students_score = {"students":students_name,
                  "scores":score_students}
print(students_score)

# Iterate through dictionary
for key, value in students_score.items():
    print(key, value, sep=": ")

# Iterate through pandas DataFrame, but iterate each column (not useful)
import pandas
frame = pandas.DataFrame(students_score)
print(frame)
print()
for key, value in frame.items():
    print(key, value, sep=": ")
print()

# Iterate each row (Series obj)
for (index, row) in frame.iterrows():
    print(index, row, sep=":")
print()

for (index, row) in frame.iterrows():
    print(index, row.scores, sep=":")