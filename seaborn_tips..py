import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a scatter plot of total_bill vs tip
plt.figure(figsize=(8, 6))  # Set the figure size
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="time", style="time", palette="viridis")

# Customize the plot
plt.title("Scatter Plot: Total Bill vs Tip", fontsize=16)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.legend(title="Time")  # Add a legend for the 'time' column

# Show the scatter plot
plt.show()

# Create a box plot of total_bill by day
plt.figure(figsize=(8, 6))  # Set the figure size
sns.boxplot(x="day", y="total_bill", data=tips, palette="pastel")

# Customize the plot
plt.title("Box Plot: Total Bill by Day", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill ($)", fontsize=12)

# Show the box plot
plt.show()