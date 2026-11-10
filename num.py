import numpy as np

# Student marks
marks = np.array([85, 90, 78, 92, 88])

# Calculate total marks
total = np.sum(marks)

# Calculate average marks
average = np.mean(marks)

# Find highest and lowest marks
highest = np.max(marks)
lowest = np.min(marks)

# Display results
print("Student Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)