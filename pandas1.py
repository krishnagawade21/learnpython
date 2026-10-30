import pandas as pd

# Create student data
data = {
    'Name': ['Krishna', 'Rahul', 'Amit', 'Sneha', 'Priya'],
    'Maths': [85, 78, 90, 88, 95],
    'Science': [80, 75, 85, 92, 89],
    'English': [75, 80, 88, 85, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete data
print("Student Records:")
print(df)

# Calculate total marks
df['Total'] = df['Maths'] + df['Science'] + df['English']

# Calculate percentage
df['Percentage'] = df['Total'] / 3

# Display students scoring above 85%
print("\nStudents scoring above 85%:")
print(df[df['Percentage'] > 85])

# Find highest percentage
print("\nHighest Percentage:")
print(df['Percentage'].max())

# Display average marks
print("\nAverage Marks:")
print(df[['Maths', 'Science', 'English']].mean())

# Sort students by percentage
print("\nStudents sorted by percentage:")
print(df.sort_values(by='Percentage', ascending=False))

# Save data to CSV
df.to_csv("student_marks.csv", index=False)

print("\nData saved successfully!")