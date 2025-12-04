import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


# Load Data
data = pd.read_excel("c:\\Users\\Lenovo\\Desktop\\student_depression_dataset.xlsx")
df = pd.DataFrame(data)
print(df.columns)
# Data Cleaning
df = df.dropna()
df = df.drop_duplicates()
df = df.reset_index(drop=True)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.nunique())
print(df.columns)
print(df.dtypes)
print(df.shape)
print(df.corr)
# Univariate Analysis
plt.pyplot.figure(figsize=(10, 6))
sns.countplot(x="Gender", data=df)
plt.pyplot.title("Gender Distribution")
plt.pyplot.show()
plt.pyplot.figure(figsize=(10, 6))
sns.countplot(x="Depression", data=df)
plt.pyplot.title("Depression Distribution")
plt.pyplot.show()
plt.pyplot.figure(figsize=(10, 6))
sns.histplot(df["Age"], bins=10, kde=True)
plt.pyplot.title("Age Distribution")
plt.pyplot.show()
plt.pyplot.figure(figsize=(10, 6))
sns.countplot(x="Work/Study Hours", data=df)
plt.pyplot.title("Work/Study Hours Distribution")
plt.pyplot.show()
plt.pyplot.figure(figsize=(10, 6))
sns.countplot(x="Financial Stress", data=df)
plt.pyplot.title("Financial Stress Distribution")
plt.pyplot.show()
# Bivariate Analysis
plt.pyplot.figure(figsize=(10, 6))
sns.boxplot(x="Depression", y="Age", data=df)
plt.pyplot.title("Age vs Depression")
plt.pyplot.show()
# Gender vs Depression Score
plt.pyplot.figure(figsize=(10, 6))
sns.boxplot(x="Gender", y="Depression", data=df)
plt.pyplot.title("Gender vs Depression")
plt.pyplot.show()
# Correlation Analysis
df_numeric = df.select_dtypes(include=['int64', 'float64'])
plt.pyplot.figure(figsize=(10, 6))
correlation_matrix = df_numeric.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.pyplot.title("Correlation Matrix")
plt.pyplot.show()
# Pie Chart:
depression_counts = df["Depression"].value_counts()
plt.pyplot.figure(figsize=(8,8))
plt.pyplot.pie(depression_counts, labels=depression_counts.index, autopct="%1.1f%%", startangle=140)
plt.pyplot.title("Depression Distribution")
plt.pyplot.show()
# Impact of Lifestyle on Depression
plt.pyplot.figure(figsize=(8, 6))
sns.boxplot(x="Sleep Duration", y="Depression", data=df)
plt.pyplot.title("Sleep Duration vs Depression")
plt.pyplot.show()
plt.pyplot.figure(figsize=(8, 6))
sns.boxplot(x="Dietary Habits", y="Depression", data=df)
plt.pyplot.title("Dietary Habits vs Depression")
plt.pyplot.show()

# Gender vs Family History of Mental Illness
# Stacked bar chart
plt.pyplot.figure(figsize=(8, 6))
gender_family = pd.crosstab(df["Gender"], df["Family History of Mental Illness"])
gender_family.plot(kind="bar", stacked=True)
plt.pyplot.title("Gender vs Family History of Mental Illness")
plt.pyplot.xlabel("Gender")
plt.pyplot.ylabel("Count")
plt.pyplot.show()

# Saved Cleaned Data
df.to_excel("cleaned_student_depression_dataset.xlsx", index=False)
print("Cleaned data saved to cleaned_student_depression_dataset.xlsx")