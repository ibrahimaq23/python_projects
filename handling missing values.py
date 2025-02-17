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

print("DataFrame after handling missing values:\n", df)

'''pd.DataFrame(data):

Converts a dictionary, list, or other data structure into a pandas DataFrame.

Each key in the dictionary becomes a column, and the values become the rows.

dropna():

Removes rows or columns with missing values.

Parameters:

how='all': Drops a row/column only if all values are missing.

inplace=True: Modifies the DataFrame directly.

fillna():

Fills missing values with a specified value or method.

Parameters:

Value: A scalar (e.g., "Unknown") or a computed value (e.g., df['Age'].median()).

inplace=True: Modifies the DataFrame directly.

median():

Computes the median (middle value) of a column.

Used to fill missing values in a way that is robust to outliers.

mean():

Computes the average of a column.

Used to fill missing values with a representative value.

'''