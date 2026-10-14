from sklearn.neural_network import MLPClassifier

# Training data: [Age, Income]
X = [[20, 20000],
    [25, 25000],
    [30, 30000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
]

# 0 = No, 1 = Yes
y = [0, 0, 0, 1, 1, 1]

# create MLP model
model = MLPClassifier(hidden_layer_sizes=(5, ), max_iter=2000)

#Train the model
model.fit(X, y)

# Get input from user
age = int(input("Enter age: "))
income = int(input("Enter income: "))

#prediction
result = model.predict([[age, income]])

if result[0] == 1:
    print("prediction: customer will BUY")
else:
    print("prediction: customer will NOT BUY")

