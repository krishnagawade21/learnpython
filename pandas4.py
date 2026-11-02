import pandas as pd

# Create student data
data = {
    'Name': ['Krishna', 'Rahul', 'Amit', 'Sneha', 'Priya'],
    'Maths': [85, 78, 90, 88, 95],
    'Science': [80, 75, 85, 90, 92],
    'English': [88, 82, 78, 85, 89]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df['Total'] = df['Maths'] + df['Science'] + df['English']

# Calculate percentage
df['Percentage'] = df['Total'] / 3

# Display DataFrame
print("Student Marks Analysis:")
print(df)

# Find topper
topper = df.loc[df['Total'].idxmax()]

print("\nTopper:")
print(topper['Name'])
print("Total Marks:", topper['Total'])
print("Percentage:", topper['Percentage'])