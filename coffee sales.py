import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv(r"D:\Unified mentor Internship projects\Coffee sales\coffee_sales.csv")

# Display the first few rows.
print(data.head())

# Display datatype of each column.
data.info()

# Display sum of null values present in each column.
data.isnull().sum()

# Display sum of duplicate values in each column 
data.duplicated().sum()

# Copied dataframe as it is for modification.
new_data = data.copy()

# number of transaction in the data as 'cash_type'.
cash_type_count = new_data['cash_type'].count()
cash_type_count

# number of transaction in the data as 'card'.
card_count = new_data['card'].count()
card_count

# count of enteries in coffee_name column.
coffee_name_count = new_data['coffee_name'].count()
coffee_name_count

# unique enteries in cash_type
cash_type_unique = new_data['cash_type'].unique()
cash_type_unique

# unique enteries in card
card_unique = new_data['card'].unique()
card_unique

# unique enteries in coffee_name
coffee_name_unique = new_data['coffee_name'].unique()
coffee_name_unique

# checking most number of null values in card column
new_data[new_data['card'].isnull()]['cash_type'].value_counts()

# Filling mising categorical values with mode.
new_data['card'].fillna(new_data['card'].mode()[0], inplace = True)
new_data

# plotting histogram for cash_type
new_data['cash_type'].hist()

# checking the most popular and second most popular products.
pd.DataFrame(new_data['coffee_name'].value_counts(normalize=True).sort_values(ascending=False).round(4)*100)

#Convert date and datetime to datetme format
new_data['date']=pd.to_datetime(new_data['date'], format = '%Y-%m-%d')
new_data['datetime']=pd.to_datetime(new_data['datetime'])

#Create column of Month, Weekdays, and Hours
new_data['month']=new_data['datetime'].dt.strftime('%Y-%m')
new_data['day']=new_data['datetime'].dt.strftime('%w')
new_data['hour']=new_data['datetime'].dt.strftime('%H')

new_data
# new column has been added to data_frame.
new_data.info()

new_data.head()

# minimum time range to maximum time range.
[new_data['datetime'].min(), new_data['datetime'].max()]

# overall revenue by products.
revenue_data=new_data.groupby(['coffee_name']).sum(['money']).reset_index().sort_values(by='money', ascending=False)
revenue_data

plt.figure(figsize=(10,4))
ax = sns.barplot(data=revenue_data, x='money', y='coffee_name', color='steelblue')
ax.bar_label(ax.containers[0], fontsize=6)
plt.xlabel('Revenue')

# overall monthly sales of the products.
monthly_sales = new_data.groupby(['coffee_name','month']).count()['date'].reset_index().rename(columns={'date':'count'}).pivot(index='month', columns='coffee_name', values='count').reset_index()
monthly_sales

# minimum and maximum sales per monthly_sales
monthly_sales.describe().T.loc[:,['min','max']]

plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_sales)
plt.legend(loc='upper left')
plt.xticks(range(len(monthly_sales['month'])), monthly_sales['month'], size='small')

# overall weekday sales of the products.
weekday_sales = new_data.groupby(['day']).count()['date'].reset_index().rename(columns={'date':'count'})
weekday_sales['day'] = weekday_sales['day'].astype(int) + 1
weekday_sales

plt.figure(figsize=(12,7))
sns.barplot(data=weekday_sales, x='day', y='count', color='steelblue')
plt.xticks(range(len(weekday_sales['day'])),['Sun','Mon','Tue','Wed','Thur','Fri','Sat'],size='small')

# 
daily_sales = new_data.groupby(['coffee_name','date']).count()['datetime'].reset_index().reset_index().rename(columns={'datetime':'count'}).pivot(index='date',columns='coffee_name',values='count').reset_index().fillna(0)
daily_sales
daily_sales.iloc[:,1:].describe().T.loc[:,['min','max']]

# Hourly sales of the products.
hourly_sales = new_data.groupby(['hour']).count()['date'].reset_index().rename(columns={'date':'count'})
hourly_sales

sns.barplot(data=hourly_sales,x='hour',y='count',color='steelblue')

hourly_sales_by_coffee = new_data.groupby(['hour','coffee_name']).count()['date'].reset_index().rename(columns={'date':'count'}).pivot(index='hour',columns='coffee_name',values='count').fillna(0).reset_index()
hourly_sales_by_coffee

fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# Flatten the array of subplots for easy iteration
axs = axs.flatten()

# Loop through each column in the DataFrame, skipping the 'Index' column
for i, column in enumerate(hourly_sales_by_coffee.columns[1:]): # Skip the first column ('Index')
 axs[i].bar(hourly_sales_by_coffee['hour'], hourly_sales_by_coffee[column])
 axs[i].set_title(f'{column}')
 axs[i].set_xlabel('Hour')
 axs[i].set_ylabel('Sales')
 
plt.tight_layout()

# Show the plot
plt.show()

# Data preperation:
new_data.to_excel('coffee_sales.xlsx', index=False,engine='openpyxl')


