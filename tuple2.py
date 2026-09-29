# Tuple Practice Program

students = (
    ("Rahul", 78, 85, 90),
    ("Amit", 65, 72, 80),
    ("Sneha", 92, 88, 95),
    ("Priya", 75, 81, 79)
)

for student in students:
    name = student[0]
    marks = student[1:]

    total = sum(marks)
    percentage = total / len(marks)

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)