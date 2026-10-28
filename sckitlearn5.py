import numpy as np
from sklearn.linear_model import LinearRegression

# Training data: hours studied
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

# Training data: marks obtained
y = np.array([20, 30, 40, 50, 60, 70])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict marks for 7 hours of study
hours = np.array([[7]])
predicted_marks = model.predict(hours)

print("Hours Studied:", hours[0][0])
print("Predicted Marks:", predicted_marks[0])