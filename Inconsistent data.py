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

# handling missing values 
# Drop rows where all values are NaN
df.dropna(how='all', inplace=True)

# Fill missing Age with the median value
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing City with "Unknown"
df['City'].fillna("Unknown", inplace=True)

# Fill missing Salary with the mean value
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Salary'] = df['Salary'].round().astype(int)  # Round and convert to integer

df.drop_duplicates(inplace=True) # Drop duplicates
print("DataFrame after handling duplicate values:\n", df) #in our data frame alice had all the attributes same as the other alice so it was dropped.

#not what we want is, to have consistent format of city coulumn, if there are any typos it will handle it as well.
df['city']=df['City'].str.lower().str.strip() #lower case and remove white spaces


print("DataFrame after handling inconsistent data:\n", df) #city column is now consistent