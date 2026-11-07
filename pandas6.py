import pandas as pd

# Create student data
data = {
    "Name": ["Krishna", "Rahul", "Amit", "Sneha", "Priya"],
    "Python": [85, 78, 92, 88, 95],
    "Java": [80, 75, 89, 90, 91],
    "AI": [90, 82, 95, 85, 93]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total marks
df["Total"] = df["Python"] + df["Java"] + df["AI"]

# Calculate percentage
df["Percentage"] = df["Total"] / 3

# Display student data
print("Student Marks:")
print(df)

# Find highest percentage
print("\nHighest Percentage:")
print(df["Percentage"].max())

# Find lowest percentage
print("\nLowest Percentage:")
print(df["Percentage"].min())

# Find topper
print("\nTopper:")
print(df.loc[df["Percentage"].idxmax()])