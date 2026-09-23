print("===== STUDENT MARKS ANALYSIS =====")

n = int(input("Enter number of subjects: "))

total = 0
passed = 0
failed = 0
highest = 0
lowest = 100

for i in range(1, n + 1):

    marks = int(input(f"Enter marks for subject {i}: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    total = total + marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if marks > highest:
        highest = marks

    if marks < lowest:
        lowest = marks

percentage = total / n

print("\n===== RESULT =====")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Passed Subjects:", passed)
print("Failed Subjects:", failed)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

if percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")

if failed == 0:
    print("Result: PASS")
else:
    print("Result: FAIL")