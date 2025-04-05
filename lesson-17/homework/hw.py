import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1. Rename columns
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print the first 3 rows
print(df.head(3))

# 3. Find the mean age
print("Mean age:", df['age'].mean())

# 4. Select and print only the 'first_name' and 'City' columns
print(df[['first_name', 'City']])

# 5. Add a new column 'Salary' with random values
import numpy as np
df['Salary'] = np.random.randint(50000, 100000, size=len(df))

# 6. Display summary statistics
print(df.describe())



# 1. Create the DataFrame
sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

# 2. Maximum values
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# 3. Minimum values
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# 4. Average values
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())



# 1. Create the DataFrame
expenses_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expenses_data)

# Set 'Category' as index
expenses.set_index('Category', inplace=True)

# 2. Max expense for each category
print("Max Expenses:\n", expenses.max(axis=1))

# 3. Min expense for each category
print("Min Expenses:\n", expenses.min(axis=1))

# 4. Average expense for each category
print("Average Expenses:\n", expenses.mean(axis=1))
