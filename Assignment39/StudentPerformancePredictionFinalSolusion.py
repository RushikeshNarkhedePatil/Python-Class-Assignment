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
#################################################################################
# 1. Loading the dataset
#################################################################################

data = pd.read_csv('student_performance_ml.csv')

#################################################################################
# 2. Data analysis
#################################################################################

print(data.head())
print(data.describe())
print(data.info())

#################################################################################
# 3. Visualization
#################################################################################

plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.hist(data['StudyHours'], bins=10, color='blue', alpha=0.7)
plt.title('Study Hours Distribution')
plt.subplot(2, 3, 2)
plt.hist(data['Attendance'], bins=10, color='green', alpha=0.7)
plt.title('Attendance Distribution')
plt.subplot(2, 3, 3)
plt.hist(data['PreviousScore'], bins=10, color='orange', alpha=0.7)
plt.title('Previous Score Distribution')
plt.subplot(2, 3, 4)
plt.hist(data['AssignmentsCompleted'], bins=10, color='red', alpha=0.7)
plt.title('Assignments Completed Distribution')
plt.subplot(2, 3, 5)
plt.hist(data['SleepHours'], bins=10, color='purple', alpha=0.7)
plt.title('Sleep Hours Distribution')
plt.tight_layout()
plt.show()

#################################################################################
# 4. Train-test split
#################################################################################
X = data.drop('FinalResult', axis=1)  # Features
y = data['FinalResult']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#################################################################################
# 5. Model training
#################################################################################
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

#################################################################################
# 6. Prediction
#################################################################################

y_pred = model.predict(X_test)

#################################################################################
# 7. Accuracy calculation
#################################################################################

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

#################################################################################
# 8. Confusion matrix generation
#################################################################################
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

#################################################################################
# 9. Final conclusion
#################################################################################
print("The model achieved an accuracy of {:.2f}, indicating that it can predict student performance with reasonable accuracy. The confusion matrix shows the distribution of true positives, true negatives, false positives, and false negatives, which can help identify areas for improvement in the model.")