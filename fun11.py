def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = calculate_grade(percentage)

    print("\n----- Student Result -----")
    print("Name:", name)

    print("Marks:")
    for i in range(len(marks)):
        print("Subject", i + 1, ":", marks[i])

    print("Total:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)

    if grade == "F":
        print("Result: Fail")
    else:
        print("Result: Pass")


# Main program
name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

display_result(name, marks)