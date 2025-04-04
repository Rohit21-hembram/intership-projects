import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

smokers = pd.read_csv(r"D:\Unified mentor Internship projects\6. Tobacco use and mortality\Tobacco Use and Mortality, 2004-2015-20241104T085210Z-001\Tobacco Use and Mortality, 2004-2015\smokers.csv")
prescriptions = pd.read_csv(r"D:\Unified mentor Internship projects\6. Tobacco use and mortality\Tobacco Use and Mortality, 2004-2015-20241104T085210Z-001\Tobacco Use and Mortality, 2004-2015\prescriptions.csv")
metrics = pd.read_csv(r"D:\Unified mentor Internship projects\6. Tobacco use and mortality\Tobacco Use and Mortality, 2004-2015-20241104T085210Z-001\Tobacco Use and Mortality, 2004-2015\metrics.csv")


# Smokers by gender.
smokers_dropped = smokers.drop(smokers.columns[1], axis = 1)
smokers_tall = pd.melt(smokers_dropped, id_vars = ["Year", "Sex"], var_name="Variable", value_name="Value")
smokers_gender = smokers_tall.groupby("Sex")["Value"].sum().reset_index()
smokers_gender.columns = ["Sex", "N"]
smokers_gender["Sex"] = pd.Categorical(smokers_gender["Sex"], categories=["NA", "Female", "Male"], ordered = True)


plt.figure(figsize = (8, 6))
sns.barplot(data = smokers_gender, x = "Sex", y = "N", hue = "Sex", dodge = False, palette = "muted")

plt.title("Number of smokers by gender")
plt.xlabel("Sex")
plt.ylabel("Number of smokers")
plt.legend(title = "Sex")
plt.grid(False)
plt.tight_layout()
plt.show()

# Smokers by Age.
smokers_age = smokers_tall.groupby("Variable")["Value"].sum().reset_index()
smokers_age.columns = ["Age", "N"]

age_labels = ["16 and over", "16-24", "25-34", "35-49", "50-59", "60 and over"]
smokers_age["Age"] = age_labels
plt.figure(figsize=(10,6))
sns.barplot(data = smokers_age, x = "Age", y = "N", palette = "muted")

plt.title("Number of smokers by age")
plt.xlabel("age group")
plt.ylabel("Number of smokers")
plt.xticks(rotation = 45, ha = "right")
plt.grid(False)
plt.gca().set_ylim(bottom = 0)

plt.tight_layout()
plt.show()

# Smokers over the years.
smokers_years = smokers_tall.groupby("Year")["Value"].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(smokers_years["Year"], smokers_years["Value"], color = "Red", linewidth = 1.5)

plt.title("Number of smokers over the year")
plt.xlabel("years")
plt.ylabel("Number of smokers")
plt.grid(True, linestyle = "--", alpha = 0.5)
plt.tight_layout()

plt.show()

# Smokers over the years by gender.
smokers_year_gender = smokers_tall.groupby(["Year", "Sex"])["Value"].sum().reset_index()
smokers_year_gender.columns = ["Year", "Sex", "N"]

smokers_year_gender["Sex"] = pd.Categorical(smokers_year_gender["Sex"], categories = ["NA", "Female", "Male"], ordered = True)

plt.figure(figsize=(10, 6))
for sex in smokers_year_gender["Sex"].unique():
    subset = smokers_year_gender[smokers_year_gender["Sex"] == sex]
    plt.plot(subset["Year"], subset["N"], label = sex, linewidth = 1.5)
    
plt.title("Number of smokers over the years by gender")
plt.xlabel("Year")
plt.ylabel("Number of smokers")
plt.legend(title = "Sex")
plt.grid(True, linestyle = "--", alpha = 0.5)
plt.tight_layout()

plt.show()

# Smokers over the years by age.
smokers_year_age = smokers_tall.groupby(["Year", "Variable"])["Value"].sum().reset_index()
smokers_year_age.columns = ["Year", "Age", "N"]

age_labels = ["16 and over", "16-24", "25-34", "35-49", "50-59", "60 and over"]
smokers_year_age["Age"] = smokers_year_age["Age"].map(dict(zip(smokers_year_age["Age"].unique(), age_labels)))

plt.figure(figsize = (12,6))
for age in smokers_year_age["Age"].unique():
    subset = smokers_year_age[smokers_year_age["Age"] == age]
    plt.plot(subset["Year"], subset["N"], label = age, linewidth = 1.5)
    
plt.title("Number of smokers over the year by age")
plt.xlabel("Year")
plt.ylabel("Number of smokers")
plt.legend(title = "Age group")
plt.grid(True, linestyle = "--", alpha = 0.5)
plt.tight_layout()

plt.show()

# Smokers over the year by gender and age.
smokers_tall["Sex"] = pd.Categorical(smokers_tall["Sex"], categories = ["NA", "Female", "Male"], ordered = True)

age_labels = ["16 and over", "16-24", "25-34", "35-49", "50-59", "60 and over"]
smokers_tall["Variable"] = smokers_tall["Variable"].map(dict(zip(smokers_tall["Variable"].unique(), age_labels)))

g = sns.FacetGrid(smokers_tall, col = "Variable", col_wrap = 3, height = 4, sharey = True)

g.map(sns.lineplot, "Year", "Value", "Sex", hue_order = ["NA", "Female", "Male"], linewidth = 0.5)

g.add_length(title = "Sex")
g.set_axis_labels("Year", "Number of smokers")
g.set_title("{col_name}")
plt.subplots_adjust(top = 0.9)
g.fig.suptitle("Number of smokers over years by age and Gender", fontsize = 16)

plt.show()

# spliting the datasets into 2 datasets, prescription number and prescription cost.
prescription_num = prescriptions.iloc[:, 0:5]
prescription_cost = prescriptions.iloc[:, [0] + list(range(5, 9))]

# Replacing NA values with 0.
prescription_num = prescription_num.fillna(0)

# reshaping the data into long format.
prescription_num_tall = prescription_num.drop(prescription_num.columns[1], axis = 1).melt(id_vars = "Year", var_name = "Medication", value_name = "Prescriptions")

# Aggregate by medication type.
prescription_num_type = prescription_num_tall.groupby("Medication")["Prescriptions"].sum().reset_index()

# Sorting by total prescription in descending order.
prescription_num_type = prescription_num_tall.sort_values("Prescriptions", ascending = False)

# customizing medication labels.
drug_labels = ["NRT", "Varencline (Champix)", "Bupropion (Zyban)"]
prescription_num_type["Medication"] = prescription_num_type["Medication"].map(dict(zip(prescription_num_type["Medication"].unique(), drug_labels)))

# Bar plot
plt.figure(figsize=(10,6))
sns.barplot(data = prescription_num_type, x = "Medication", y = "Prescriptions", palette = ["darkblue", "darkred", "darkorange"])

plt.title("Smoking medication prescriptions")
plt.xlabel("Medication type")
plt.ylabel("Number of prescriptions")
plt.grid(False)
plt.tight_layout()

plt.show()