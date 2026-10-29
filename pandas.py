import numpy as np
import pandas as pd

# 1. Create a DataFrame from a dictionary
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [70000, 85000, np.nan, 95000, 72000],  # Includes a missing value
    "Experience_Years": [3, 5, 2, 8, 4],
}

df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)
print("\n")

# 2. Data Cleaning: Fill missing salary values with the average salary
mean_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(mean_salary)
print("--- After Cleaning (Filled Missing Salary) ---")
print(df)
print("\n")

# 3. Data Manipulation: Add a new column based on a condition
# Employees with 5+ years of experience get a 10% bonus, others get 5%
df["Bonus_Pct"] = np.where(df["Experience_Years"] >= 5, 0.10, 0.05)
df["Total_Compensation"] = df["Salary"] * (1 + df["Bonus_Pct"])

# 4. Data Filtering: Select employees who make more than $75,000
high_earners = df[df["Total_Compensation"] > 75000]
print("--- High Earners (> $75k Total Compensation) ---")
print(high_earners)
print("\n")

# 5. Data Aggregation: Find the average total compensation by Department
dept_summary = (
    df.groupby("Department")["Total_Compensation"].mean().reset_index()
)
print("--- Average Compensation by Department ---")
print(dept_summary)