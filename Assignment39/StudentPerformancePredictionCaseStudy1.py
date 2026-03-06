# 1. Import DecisionTreeClassi er from sklearn.
# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

Border = "*"*50
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

# Prepare the data for training
# df.drop('FinalResult', axis=1) removes the 'FinalResult' column from the DataFrame and returns the remaining columns as features (X).
X = df.drop('FinalResult', axis=1)  # Features
y = df['FinalResult']  # Target variable labels

print(Border)
print("Data prepared for training.")
print("Features (X):\n", X.head())
print("Target variable (y):\n", y.head())
print(Border)

# Create a Decision Tree Classifier model
model = DecisionTreeClassifier()
# Train the model using fit()
model.fit(X, y)
#print("Model trained successfully.")

# 2. Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

# Predict results for the training data (X)
y_pred = model.predict(X)

print("Predicted values:\n", y_pred)
print("Actual values:\n", y.values)
print(Border)

# 3. Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

from sklearn.metrics import accuracy_score
# Calculate accuracy

accuracy = accuracy_score(y, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 4. Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.
# Explain clearly:
# •True Positive
# •True Negative
# •False Positive
# •False Negative

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Generate confusion matrix
cm = confusion_matrix(y, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap='Blues')
import matplotlib.pyplot as plt
plt.title("Confusion Matrix")
plt.show()