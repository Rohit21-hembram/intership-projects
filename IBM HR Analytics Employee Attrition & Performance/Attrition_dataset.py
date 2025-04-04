# Importing libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading dataset.
df = pd.read_csv(r"D:\Unified mentor Internship projects\4. IBM HR analytics employee attri. & perfomance\WA_Fn-UseC_-HR-Employee-Attrition.csv")

# checking the dataset.
df.head()

# Checking data shape.
df.shape

# Checking duplicated values.
df.duplicated().sum()

# Checking missing values.
df.isnull().sum()

# checking the datatypes.
df.dtypes

# Checking for any apparent outliers in the dataset.
df.describe()

# EDA
# Attrition rate 
attrition = df['Attrition'].value_counts(normalize = True)

plt.figure(figsize = (8,6))
ax = sns.barplot(x = attrition.index, y = attrition)

for i in ax.patches:
    ax.annotate (f'{i.get_height() * 100:.2f}%',
                 (i.get_x() + i.get_width() / 2., i.get_height()),
                 ha = 'center', va = 'bottom')

plt.title('Distribution of Attrition Rate')
plt.xlabel('Attrition')
plt.ylabel('percentage')
plt.tight_layout()
plt.show()

# Average of Tenure.
avg_tenure = df['YearsAtCompany'].mean()
avg_tenure

# Employee Demographics
fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (15,5))

sns.histplot(data = df, x = 'Age', kde = True, ax = axes[0])
axes[0].set_title('Distribution Employee by Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Count')

sns.countplot(data = df, x = 'Gender', ax = axes[1])
axes[1].set_title('Distribution employee by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Count')

sns.countplot(data = df, x = 'Department', ax = axes[2])
axes[2].set_title('Distribution Employee by Department')
axes[2].set_title('Gender')
axes[2].set_ylabel('Count')

plt.tight_layout()
plt.show()

# A dataset only containing Attrition employees.
df_attrition = df[df['Attrition'] == 'Yes']
df_attrition.head()

# 
def calculate_attrition_rate(df, column): 
    attrition_counts = df.groupby([column, 'Attrition']).size().unstack(fill_value = 0)
    attrition_rate = attrition_counts['Yes'] / attrition_counts.sum(axis = 1) * 100
    attrition_rate_df = attrition_rate.reset_index()
    attrition_rate_df.columns = [column, 'AttritionRate']
    return attrition_rate_df

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (15, 6))

sns.kdeplot(data = df_attrition, x = 'Age', fill = True, ax = axes[0])
axes[0].set_title('Attrition by Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Density')

attrition_rate_df = calculate_attrition_rate(df, 'Gender')
sns.barplot(data = attrition_rate_df, x = 'Gender', y = 'AttritionRate', ax = axes[1])
axes[1].set_title('Attrition by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Attrition Rate (%)')

plt.tight_layout()
plt.show()

# Data_preperation.
df.to_excel('Employee_Attrition.xlsx', index = False, engine = 'openpyxl')
