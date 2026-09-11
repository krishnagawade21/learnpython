# Function to calculate total marks
def calculate_total(marks):
    total = sum(marks)
    return total


# Function to calculate percentage
def calculate_percentage(total, subjects):
    percentage = total / subjects
    return percentage


# Function to check result
def check_result(percentage):
    if percentage >= 40:
        return "PASS"
    else:
        return "FAIL"


# Main program
while True:

    print("\n===== STUDENT MARKS =====")

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = calculate_total(marks)
    percentage = calculate_percentage(total, 5)
    result = check_result(percentage)

    print("\n----- RESULT -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Result:", result)

    choice = input("\nDo you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Program ended.")
        break