# 1. Write a Python program to load the le student_performance_ml.csv using pandas.
# Display:
# First 5 records
# Last 5 records
# Total number of rows and columns
# List of column names
# Data types of each column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = 'student_performance_ml.csv'
df = pd.read_csv(file_path)

Border = "-"*100
print(Border)

# Display First Five Record used head() to show first five records
print("First Five Rows Data is : \n",df.head())

# Display Last Five Record. tail() method used to show by default last five row.
print("Last Five Rows Data is : \n",df.tail())

# Total number of rows and columns dataframe.shape[0] indicate total rows side and shape[1] show column size.
print(f"Total number of rows is : {df.shape[0]} and columns are : ",df.shape[1])

# List of column names
print("List of Column Names is : \n",list(df.columns))

# Data types of each column
print("Show Data Types of each column :\n",df.dtypes)

print(Border)

# 2. Write a program to:
# Display total number of students in the dataset
# Count how many students Passed (FinalResult = 1)
# Count how many students Failed (FinalResult = 0)

print("Display total number of students in the dataset : ",df.shape[0])

print("Count how many students Passed (FinalResult = 1) : ",list(df["FinalResult"]).count(1))

print("Count how many students Failed (FinalResult = 0) : ",list(df["FinalResult"]).count(0))

print(Border)

# 3. Using pandas functions, calculate and display:
# Average StudyHours
# Average Attendance
# Maximum PreviousScore
# Minimum SleepHours
print(Border)
print("Average StudyHours : ",df["StudyHours"].mean())
print("Average Attendance : ",df["Attendance"].mean())
print("Average PreviousScore : ",df["PreviousScore"].mean())
print("Average SleepHours : ",df["SleepHours"].mean())

print(Border)

# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

Resultstudent = df["FinalResult"].value_counts(True)

print("Pass Student Persentage :",Resultstudent[1])
print("Fail Student Persentage :",Resultstudent[0])
#print(failstudent)
print(Border)

# 6. Plot a histogram of StudyHours.
plt.title("Student Study Hours")
plt.hist(df["StudyHours"])
plt.show()
print(Border)

# 7. Create a scatter plot of:
# StudyHours vs PreviousScore
plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
sns.scatterplot(x = df["StudyHours"],y = df["PreviousScore"],hue=df["FinalResult"])
plt.legend() # show status window which color show on which type of result.
plt.show()

# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.

plt.boxplot(x=df["Attendance"])
plt.show()

# 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

sns.scatterplot(x=df["AssignmentsCompleted"], y = df["FinalResult"],hue=df["FinalResult"])
plt.title("relationship between AssignmentsCompleted and FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.legend()
plt.show()

# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.
sns.scatterplot(x=df["SleepHours"], y = df["FinalResult"],hue=df["FinalResult"])
plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.legend()
plt.show()