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

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

Border = "*" * 80
print(Border)
print("Student Performance Prediction using Decision Tree Classifier")
print(Border)
#################################################################################
# 1. Loading the dataset
#################################################################################

data = pd.read_csv('student_performance_ml.csv')
print("Dataset loaded successfully!")

#################################################################################
# 2. Data analysis
#################################################################################
print(Border)
print("Data Analysis:")
print(Border)
print(data.head())
print(data.describe())
print(data.info())


#################################################################################
# 4. Train-test split
#################################################################################

print(Border)
print("Train-Test Split:")
print(Border)
X = data.drop('FinalResult', axis=1)  # Features
y = data['FinalResult']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#################################################################################
# 5. Model training
#################################################################################

print(Border)
print("Model Training:")
print(Border)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
#################################################################################

# 1. After training the Decision Tree model, use:
# model.feature_importances_
# Display importance score of each feature.
# Which feature contributes the most in predicting FinalResult?
# Which feature contributes the least?

print(Border)
print("Feature Importance:")
print(Border)
feature_importances = model.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print(importance_df)

#################################################################################

# 2. Remove the column SleepHours from the dataset.
# •Train the model again.
# •Compare new accuracy with previous accuracy.
# •Does removing this feature affect performance?

print(Border)
print("Removing SleepHours and Retraining:")
print(Border)

X = data.drop(['FinalResult', 'SleepHours'], axis=1)  # Removing SleepHours
y = data['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy after removing SleepHours: {accuracy * 100:.2f}%')

###################################################################################

# 3. Train the model using only:
# •StudyHours
# •Attendance
# Compare the accuracy with the full-feature model.
# Is the model still performing well?

print(Border)
print("Training with only StudyHours and Attendance:")
print(Border)

X = data[['StudyHours', 'Attendance']]  # Using only StudyHours and Attendance
y = data['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy using only StudyHours and Attendance: {accuracy * 100:.2f}%')

#################################################################################

# 4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

print(Border)
print("Predicting for New Students:")
print(Border)

new_students = pd.DataFrame({
    'StudyHours': [5, 3, 8, 2, 6],
    'Attendance': [90, 80, 95, 70, 80]
})

predictions = model.predict(new_students)
new_students['PredictedResult'] = predictions
print(new_students)

###############################################################################

# 5. Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

print(Border)
print("Manual Accuracy Calculation:")
print(Border)

print(y_test.values)
print(y_pred)

correct_predictions = sum(y_test == y_pred)
print(f'Correct Predictions: {correct_predictions}')
total_predictions = len(y_test)
print(f'Total Predictions: {total_predictions}')
manual_accuracy = correct_predictions / total_predictions
print(f'Manual Accuracy: {manual_accuracy * 100:.2f}%')

####################################################################################

# 6. Identify students where:
# y_test != y_pred
# •Display those rows.
# •How many students were misclassi ed?
# •What common pattern do you observe?

print(Border)
print("Misclassified Students:")
print(Border)

misclassified = X_test[y_test != y_pred]
misclassified['ActualResult'] = y_test[y_test != y_pred]
misclassified['PredictedResult'] = y_pred[y_test != y_pred]
print(misclassified)
num_misclassified = len(misclassified)
print(f'Number of Misclassified Students: {num_misclassified}')

######################################################################################

# 7. Train model using:
# •random_state = 0
# •random_state = 10
# •random_state = 42
# Compare testing accuracy.
# Does the result change?

print(Border)
print("Comparing Different Random States:")
print(Border)

for state in [0, 10, 42]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=state)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Random State: {state}, Accuracy: {accuracy * 100:.2f}%')

########################################################################################

# 8. Decision Tree Visualization
# Use:
from sklearn.tree import plot_tree
# Visualize the trained decision tree.
# •Which feature appears at the root node?
# •Why do you think that feature was selected rst?

print(Border)
print("Decision Tree Visualization:")
print(Border)

plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=['Fail', 'Pass'], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

#####################################################################################

# 9. Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance
# Train the model including this new feature.
# Does accuracy improve?

print(Border)
print("Adding PerformanceIndex and Retraining:")
print(Border)

data['PerformanceIndex'] = (data['StudyHours'] * 2) + data['Attendance']
X = data.drop('FinalResult', axis=1)
y = data['FinalResult']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy after adding PerformanceIndex: {accuracy * 100:.2f}%')

#######################################################################################

# 10. Train model with:
# •
# max_depth = None
# Calculate:
# •Training accuracy
# •Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

print(Border)
print("Training with max_depth=None:")
print(Border)

model = DecisionTreeClassifier(random_state=42, max_depth=None)
model.fit(X_train, y_train)
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f'Training Accuracy: {train_accuracy * 100:.2f}%')
print(f'Testing Accuracy: {test_accuracy * 100:.2f}%')

print(Border)
print("Notes :- If training accuracy is 100% but testing accuracy is lower, " \
"it indicates that the model is overfitting. This means the model has learned the training data too well," \
" including noise and outliers, which does not generalize well to unseen data (testing data). As a result, " \
"while it performs perfectly on the training set, " \
"it fails to make accurate predictions on the test set, leading to lower testing accuracy.")
print(Border)