def calculate_total(marks):
    # calculate and return total
    pass


def calculate_percentage(total):
    # calculate and return percentage
    pass


def find_grade(percentage):
    # return grade according to percentage
    pass


# Main program
marks = []

for i in range(5):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = find_grade(percentage)

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)