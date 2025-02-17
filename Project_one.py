import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
from prophet import Prophet

# define file path 
file_path = r"C:\Users\ibrah\OneDrive\Desktop\data analysis 101\portfolio_projects\Sample - Superstore.csv"
# Load the data
df = pd.read_csv(file_path, encoding="latin1")  # Common for CSV files with special characters

print(df.info())
print(df.isnull().sum())
print(df.describe())
# our data has no missing values
# let's check for duplicates
print(df.duplicated().sum())
# our data has no duplicates
# let's check for unique values
print(df.nunique())

# lets clean data 
# Convert Order Date and Ship Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Now, extract the month and calculate delivery time
df["Order Month"] = df["Order Date"].dt.month  # Extract month
df["Delivery Time"] = (df["Ship Date"] - df["Order Date"]).dt.days  # Delivery days

# Convert Postal Code to string
df["Postal Code"] = df["Postal Code"].astype(str)
# Aggregate sales and profits over time
df['Order Year'] = df['Order Date'].dt.year  # Extract year
monthly_sales = df.groupby(['Order Year', 'Order Month'])[['Sales', 'Profit']].sum().reset_index()

# Plot Sales and Profit Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Order Month', y='Sales', hue='Order Year', marker='o', palette='coolwarm')
plt.title("Total Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.legend(title="Year")
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Order Month', y='Profit', hue='Order Year', marker='o', palette='coolwarm')
plt.title("Total Profits Over Time")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.legend(title="Year")
plt.show()
# Top 10 Products by Sales
top_products = df.groupby("Product Name")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(y=top_products.index, x=top_products["Sales"], palette="Blues_r")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()
# Top Categories by Profit
top_categories = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(by="Profit", ascending=False)

plt.figure(figsize=(8, 6))
sns.barplot(y=top_categories.index, x=top_categories["Profit"], palette="Greens_r")
plt.title("Most Profitable Categories")
plt.xlabel("Total Profit")
plt.ylabel("Category")
plt.show()
# Sales and Profit by Region
region_sales_profit = df.groupby("Region")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(y=region_sales_profit.index, x=region_sales_profit["Sales"], palette="Reds_r")
plt.title("Top Regions by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Region")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(y=region_sales_profit.index, x=region_sales_profit["Profit"], palette="Purples_r")
plt.title("Top Regions by Profit")
plt.xlabel("Total Profit")
plt.ylabel("Region")
plt.show()
# Customer Segmentation
customer_analysis = df.groupby("Customer ID")[["Sales", "Profit", "Order ID"]].agg({
    "Sales": "sum",
    "Profit": "sum",
    "Order ID": "count"
}).rename(columns={"Order ID": "Total Orders"}).sort_values(by="Sales", ascending=False)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=customer_analysis["Sales"], y=customer_analysis["Profit"], size=customer_analysis["Total Orders"], sizes=(10, 200), alpha=0.7)
plt.title("Customer Segmentation: Sales vs Profit")
plt.xlabel("Total Sales")
plt.ylabel("Total Profit")
plt.show()
# Monthly Sales Trend
monthly_sales_trend = df.groupby("Order Month")[["Sales", "Profit"]].sum().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales_trend, x="Order Month", y="Sales", marker="o", label="Sales", color="blue")
sns.lineplot(data=monthly_sales_trend, x="Order Month", y="Profit", marker="o", label="Profit", color="red")
plt.title("Monthly Sales & Profit Trends")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()


df.to_csv(r"C:\Users\ibrah\OneDrive\Desktop\data analysis 101\portfolio_projects\processed_superstore.csv", index=False)
