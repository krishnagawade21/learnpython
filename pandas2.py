import pandas as pd

# Create student data
data = {
    'Name': ['Krishna', 'Rahul', 'Amit', 'Sneha', 'Priya'],
    'Python': [85, 90, 75, 95, 80],
    'Java': [80, 85, 70, 90, 75],
    'DBMS': [90, 80, 85, 95, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df['Total'] = df[['Python', 'Java', 'DBMS']].sum(axis=1)

# Calculate percentage
df['Percentage'] = df['Total'] / 3

# Assign grades
def grade(per):
    if per >= 90:
        return 'A'
    elif per >= 80:
        return 'B'
    elif per >= 70:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Percentage'].apply(grade)

# Display complete DataFrame
print("Student Marks Analysis:")
print(df)

# Display topper
print("\nTopper:")
print(df.loc[df['Total'].idxmax()])

# Display average percentage
print("\nAverage Percentage:")
print(df['Percentage'].mean())