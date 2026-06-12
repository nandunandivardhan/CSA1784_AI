from sklearn.neural_network import MLPClassifier

# Training Data
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

# Create Feed Forward Neural Network
model = MLPClassifier(hidden_layer_sizes=(4,),
                      max_iter=1000,
                      random_state=1)

# Train Model
model.fit(X, y)

# Predict
n = float(input("Enter a value: "))
print("Prediction:", model.predict([[n]])[0])
