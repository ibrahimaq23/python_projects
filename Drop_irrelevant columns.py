import numpy as np
import pandas as pd

# Create a dirty dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", np.nan, "Alice"],
    "Age": [25, 30, 35, 40, 28, 33, np.nan, 25],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", np.nan, "Chicago", "Miami", "New York"],
    "Salary": [50000, 60000, 70000, np.nan, 55000, 65000, 80000, 50000],
    "Department": ["HR", "Finance", "IT", "IT", "HR", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)

print("Dirty DataFrame:\n", df)

# Handling missing values
# Drop rows where all values are NaN
df.dropna(how='all', inplace=True)

# Fill missing Age with the median value
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing City with "Unknown"
df['City'].fillna("Unknown", inplace=True)

# Fill missing Salary with the mean value
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Salary'] = df['Salary'].round().astype(int)  # Round and convert to integer

# Drop duplicates
df.drop_duplicates(inplace=True)

# Standardize the City column (convert to lowercase and strip whitespace)
df['City'] = df['City'].str.lower().str.strip()

print("DataFrame after handling inconsistent data:\n", df)

# Drop irrelevant columns
df.drop(columns=['Department'], inplace=True)

print("DataFrame after dropping irrelevant columns:\n", df)