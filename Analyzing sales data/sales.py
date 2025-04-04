# importing required libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from sklearn.preprocessing import LabelEncoder

# Loading a csv file.
df = pd.read_csv(r"D:\Unified mentor Internship projects\Analyzing sales data\amazon.csv")

# Setting the option to show maximum columns.
pd.set_option('display.max_columns', None)

# Top 5 rows of the data.
df.head()

# columns name.
df.columns

# columns and their datatypes
df.info()

# shape of the data set.
df.shape

# finding out number of null values present in each column.
df.isnull().sum()

# changing data types of columns from object to float.
# changing data type of discounted price and actual price.
df['discounted_price'] = df['discounted_price'].str.replace("₹", '')
df['discounted_price'] = df['discounted_price'].str.replace(",", '')
df['discounted_price'] = df['discounted_price'].astype('float64')

# changing type of actual price.
df['actual_price'] = df['actual_price'].str.replace("₹", '')
df['actual_price'] = df['actual_price'].str.replace(",", '')
df['actual_price'] = df['actual_price'].astype('float64')

# changing values and datatype in discount_percentage.
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype('float64')
df['discount_percentage'] = df['discount_percentage'] / 100

# changing data type of rating_count and filling the null values.
df['rating_count'] = pd.to_numeric(df['rating_count'].str.replace(",", ''))
df['rating_count'] = df['rating_count'].fillna(df['rating_count'].median())

# checking number of null values.
df['rating_count'].isnull().sum()

# counting values in rating column.
df['rating'].value_counts()

# Replacing the value in rating column.
df.loc[df['rating'] == '|', 'rating'] = '4.0'

# actual_price vs rating.
plt.scatter(df['actual_price'], df['rating'])
plt.xlabel('Actual_price')
plt.ylabel('Ratings')
plt.show()

# plot distribution of actual price.
plt.hist(df['actual_price'])
plt.xlabel('actual_price')
plt.ylabel('frequency')
plt.show()

# Heat map.
new_product_id = LabelEncoder()
new_category = LabelEncoder()
new_review_id = LabelEncoder()
new_review_content = LabelEncoder()
new_product_name = LabelEncoder()
new_user_name = LabelEncoder()
new_about_product = LabelEncoder()
new_user_id = LabelEncoder()
new_review_title = LabelEncoder()
new_img_link = LabelEncoder()
new_product_link = LabelEncoder()

df['product_id'] = new_product_id.fit_transform(df['product_id'])
df['category'] = new_category.fit_transform(df['category'])
df['review_id'] = new_review_id.fit_transform(df['review_id'])
df['review_content'] = new_review_content.fit_transform(df['review_content'])
df['product_name'] = new_product_name.fit_transform(df['product_name'])
df['user_name'] = new_user_name.fit_transform(df['user_name'])
df['about_product'] = new_about_product.fit_transform(df['about_product'])
df['user_id'] = new_user_id.fit_transform(df['user_id'])
df['review_title'] = new_review_title.fit_transform(df['review_title'])
df['img_link'] = new_img_link.fit_transform(df['img_link'])
df['product_link'] = new_product_link.fit_transform(df['product_link'])

correlation_matrix = df.corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot = True)
plt.show()

# correlation analysis.
correlation_matrix = df.corr()
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm')
plt.title('correlation_matrix(pearson)')
plt.show()

# Calculate Spearman correlation coefficients (for non-linear relationships)
spearman_correlation_matrix = df.corr(method="spearman")

# Print the Spearman correlation matrix
print(spearman_correlation_matrix)

# Create a heatmap to visualize the Spearman correlations
sns.heatmap(spearman_correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix (Spearman)")
plt.show()

# correlation coefficient between product price and 
print(df[['actual_price', 'rating']].dtypes)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

correlation_coefficient = np.corrcoef(df['actual_price'], df['rating'])[0, 1]
print(correlation_coefficient)

# calculating mean sales by product category.
grouped_df = df.groupby('category')['rating'].mean()
print(grouped_df)


# Analyzing top 10 performing products by ratings.
top_rated_products = df.sort_values(by = 'rating', ascending = False).head(10)
top_rated_products[['product_name', 'rating']]

# Analyzing top 10 high demand products.
high_demand_products = df.sort_values(['rating_count', 'rating'], ascending = False).head(10)
high_demand_products[['product_name', 'category', 'rating_count', 'rating']]

# Analyzing top 10 low demand products.
low_performing_products = df[(df['rating_count'] < 100) & (df['discount_percentage'] > 0.5)].head(10)
low_performing_products[['product_name', 'category', 'rating_count', 'discount_percentage']]

# Data preperation.
df.to_excel('amazon_sales.xlsx', index=False,engine='openpyxl')

# TOP RATING_COUNT PRODUCTS BY CATEGORY.
#- The output highlights products likely to be popular within their categories based on high review counts, suggesting customer interest and engagement.
#- Review counts range from 9 to 15867, implying varying levels of attention and feedback across products.
#- Most listed products have ratings above 3.5, indicating a generally positive customer experience.
#- Products with the highest review counts within their categories might be considered potential top sellers, even without direct sales data.

# AVERAGE DISCOUNT PERCENTAGE ACROSS DIFFERENT CATEGORIES.
#- Average discount percentages vary widely across categories, ranging from 0% to 78.39%.¶
#- Categories 1 and 3 stand out with notably higher average discounts (78.39% and 56.34%), suggesting potential factors like clearance efforts, high competition, or lower-profit margins.
#- Categories 0, 206, 207, 210 have average discounts of 0%, indicating consistent pricing or strong demand for products within those categories.
#- Other categories exhibit varying discount percentages, likely reflecting diverse pricing strategies and market dynamics.

# CORRELATION BETWEEN DISCOUNTED_PRICE AND RATINGS.
#-Discounted price and rating have a weak positive correlation. This means that products with higher discounted prices tend to have slightly higher ratings, but the relationship is not very strong.

