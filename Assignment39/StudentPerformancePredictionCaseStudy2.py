# 1. Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

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


X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42  #  fix random position every time
)
# Train the model using fit()
model.fit(X_train, Y_train)
#print("Model trained successfully.")

# 2. Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

# Predict results for the testing data (X_test)
y_pred = model.predict(X_test)

print("Predicted values:\n", y_pred)
print("Actual values:\n", Y_test.values)
print(Border)

# 3. Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

from sklearn.metrics import accuracy_score
# Calculate accuracy

accuracy = accuracy_score(Y_test, y_pred)
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
cm = confusion_matrix(Y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap='Blues')
import matplotlib.pyplot as plt
plt.title("Confusion Matrix")
plt.show()

# 5. Calculate:
# Training accuracy
# Testing accuracy
# Compare both and comment whether the model is over fitting or under fitting.

# Calculate training accuracy
y_train_pred = model.predict(X_train)
training_accuracy = accuracy_score(Y_train, y_train_pred)
print(f"Training Accuracy: {training_accuracy * 100:.2f}%")

# Calculate testing accuracy
testing_accuracy = accuracy_score(Y_test, y_pred)
print(f"Testing Accuracy: {testing_accuracy * 100:.2f}%")

# 6. Train three Decision Tree models with:
# max_depth = 1
# max_depth = 3
# max_depth = None
# Compare their testing accuracies and write your observations.

# Train Decision Tree models with different max_depth values
depths = [1, 3, None]
for depth in depths:
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, y_pred)
    print(f"Testing Accuracy with max_depth={depth}: {accuracy * 100:.2f}%")

# 7. Use the trained model to predict result for a student with:
#  StudyHours = 6
#  Attendance = 85
#  PreviousScore = 66
#  AssignmentsCompleted = 7
#  SleepHours = 7
# Will the student Pass or Fail?

# Create a DataFrame for the new student

new_student = pd.DataFrame({
    'StudyHours': [6],
    'Attendance': [85],
    'PreviousScore': [66],
    'AssignmentsCompleted': [7], 
    'SleepHours': [7]  
})
# Predict the result for the new student
predicted_result = model.predict(new_student)
print(f"Predicted result for the new student: {predicted_result[0]}")

# 8. Write a single structured Python program that performs:
# 1.Dataset loading
# 2.Data analysis
# 3.Visualization
# 4.Train-test split
# 5.Model training
# 6.Prediction
# 7.Accuracy calculation
# 8.Confusion matrix generation
# 9.Final conclusion
# Your code should include proper comments explaining each step.

