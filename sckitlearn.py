import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Dataset: Hours studied and marks obtained
X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([15, 20, 30, 40, 45,
              55, 65, 75, 85, 95])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the Machine Learning model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict marks for test data
y_pred = model.predict(X_test)

# Display predictions
print("Actual Marks:", y_test)
print("Predicted Marks:", y_pred)

# Calculate model error
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Predict marks for a student studying 7 hours
hours = np.array([[7]])
predicted_marks = model.predict(hours)

print("Predicted marks for 7 hours of study:",
      round(predicted_marks[0], 2))