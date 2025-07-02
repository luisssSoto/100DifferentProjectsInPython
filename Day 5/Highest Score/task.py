student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# sum()
print(sum(student_scores))

# different approach for loo
total = 0
for score in student_scores:
    total += score
print(total)

# 1. Max
print(max(student_scores))

max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)