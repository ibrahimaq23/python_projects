import pandas as pd
#creating data frame from dictionary.
data= {'Name':['Tom', 'Jerry', 'Mickey', 'Donald'],
       'Age':[20, 21, 22, 23],
       'city':['New York', 'Los Angeles', 'Chicago', 'Houston']}
df=pd.DataFrame(data)
print(df)


'''A **DataFrame** is a fundamental data structure in the **pandas** library in Python. It is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Think of it as a spreadsheet or SQL table in memory.

### Purpose of a DataFrame:
1. **Organize Data**:
   - A DataFrame allows you to store and manipulate structured data in a tabular format (rows and columns).
   - Each column can hold data of a different type (e.g., integers, strings, floats).

2. **Data Manipulation**:
   - You can perform operations like filtering, sorting, grouping, and aggregating data easily.
   - It provides powerful tools for cleaning and transforming data.

3. **Data Analysis**:
   - DataFrames are designed for data analysis tasks, such as computing statistics, handling missing data, and merging datasets.

4. **Integration with Other Tools**:
   - DataFrames can be easily converted to/from other data structures like NumPy arrays, dictionaries, or CSV files.
   - They integrate well with visualization libraries (e.g., Matplotlib, Seaborn) and machine learning libraries (e.g., Scikit-learn).

5. **Handling Large Datasets**:
   - DataFrames are optimized for performance, making them suitable for working with large datasets.

### Why Do We Need It?
- **Ease of Use**: DataFrames provide a high-level, intuitive interface for working with structured data.
- **Efficiency**: They are optimized for performance, especially for operations on large datasets.
- **Versatility**: You can perform a wide range of data operations, from simple filtering to complex transformations.
- **Interoperability**: DataFrames can easily interact with other data science tools and libraries.

### Example Use Cases:
- Loading data from a CSV file and performing analysis.
- Cleaning and preprocessing data for machine learning.
- Aggregating data to compute summary statistics.
- Merging multiple datasets for analysis.

In your example:
```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
```
The DataFrame organizes the data into a table with rows and columns, making it easy to work with and analyze. For instance, you can:
- Filter rows based on age (`df[df['Age'] > 30]`).
- Add new columns (`df['Country'] = 'USA'`).
- Compute statistics (`df['Age'].mean()`).

Without a DataFrame, you would need to write more complex code to handle such operations.'''
