

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)

total = 0
for score in student_scores:
    total += score

#print(total)

print(max(student_scores))


maximum = 0
for number in student_scores:
    if  maximum <= number:
        maximum = number

print(maximum)
