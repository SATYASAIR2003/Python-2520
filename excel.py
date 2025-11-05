import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_excel("Cleaned_Student_Mental_Health.xlsx")
df = pd.read_csv("Cleaned_Student_Mental_Health.xlsx.csv")

# To show first few rows
print(df.head()) 

# To check basic info
print(df.info())

# Summary statistics
print(df.describe())

print("="*50)

# Count of categorical values (e.g., Gender, Anxiety)
print(df['Gender'].value_counts())
print(df['Anxiety_Level'].value_counts())
print("="*50)
# print(df['Anxiety_Level'].sort_values())

#  Checking for missing values
print(df.isnull().sum())

# To check relationships between numeric variables:

# In the below code I got error due to giving all the columns which contains 
# both string and integer values which cannot be caluculated in python
# plt.figure(figsize=(8,5))
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap – Student Mental Health")
# plt.show()

plt.figure(figsize=(8,5))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap – Student Mental Health")
plt.show()

# Sleep vs. Stress Visualization
plt.figure(figsize=(7,5))
sns.scatterplot(x='Sleep_Hours_Per_Day', y='Stress_Level', hue='Gender', data=df)
plt.title("Sleep Hours vs Stress Level by Gender")
plt.show()

# Anxiety Level Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Anxiety_Level', data=df, palette='viridis')
plt.title("Distribution of Anxiety Levels")
plt.show()

# Average Stress by Gender
plt.figure(figsize=(6,4))
sns.barplot(x='Gender', y='Stress_Level', data=df, estimator=np.mean, palette='Set2')
plt.title("Average Stress Level by Gender")
plt.show()

# Average Sleep by Course
plt.figure(figsize=(8,4))
sns.barplot(x='Course', y='Sleep_Hours_Per_Day', data=df, estimator=np.mean)
plt.xticks(rotation=45)
plt.title("Average Sleep Hours by Course")
plt.show()
print("All libraries installed successfully!")

# Save Processed Data (Optional)
df.to_excel("Processed_Student_Mental_Health.xlsx", index=False)