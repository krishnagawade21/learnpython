
from sklearn.linear_model import LogisticRegression

# Training data: hours studied
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict for a student who studies 4.5 hours
hours = [[4.5]]
prediction = model.predict(hours)

# Display the result
if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")

