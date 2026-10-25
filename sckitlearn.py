```python
from sklearn.linear_model import LogisticRegression

# Training data: hours studied
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Output: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

# Create the Machine Learning model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict result for a student who studies 6 hours
hours = [[6]]
prediction = model.predict(hours)

# Display the result
if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")
```
