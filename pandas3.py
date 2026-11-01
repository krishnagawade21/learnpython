import pandas as pd

# Create student data
data = {
    'Name': ['Krishna', 'Rahul', 'Amit', 'Sneha', 'Priya'],
    'Maths': [85, 70, 90, 65, 95],
    'Science': [80, 75, 85, 70, 90],
    'English': [75, 80, 88, 60, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df['Total'] = df['Maths'] + df['Science'] + df['English']

# Calculate percentage
df['Percentage'] = df['Total'] / 3

# Display complete data
print("Student Performance:")
print(df)

# Display students scoring above 80%
print("\nStudents scoring above 80%:")
print(df[df['Percentage'] > 80])

# Sort students by percentage
print("\nStudents sorted by percentage:")
print(df.sort_values(by='Percentage', ascending=False))

# Find average marks
print("\nAverage Marks:")
print(df['Total'].mean())

# Find highest percentage
print("\nHighest Percentage:")
print(df['Percentage'].max())

# Find lowest percentage
print("\nLowest Percentage:")
print(df['Percentage'].min())