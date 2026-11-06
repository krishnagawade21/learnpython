import pandas as pd

data = {
    'Name': ['Krishna', 'Rahul', 'Amit', 'Rohit'],
    'Maths': [85, 90, 78, 88],
    'Science': [80, 85, 82, 90],
    'English': [75, 80, 85, 92]
}

df = pd.DataFrame(data)

df['Total'] = df['Maths'] + df['Science'] + df['English']

df['Average'] = df['Total'] / 3

print("Student Marks:")
print(df)

print("\nHighest Total Marks:")
print(df['Total'].max())

print("\nLowest Total Marks:")
print(df['Total'].min())