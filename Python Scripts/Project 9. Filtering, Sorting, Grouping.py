import pandas as pd

# Create a DataFrame with sample data
data = pd.DataFrame({
    'Name': ['Anna', 'Karen', 'John', 'Alice', 'Kevin', 'Sanna', 'Bob', 'Emily'],
    'Age': [35, 30, 57, 25, 19, 20, 65, 45],
    'Salary': [20000, 60000, 145000, 170000, 30000, 10000, 220000, 120000],
    'Department': ['Tech', 'Tech', 'Tech', 'Healthcare', 'Operations', 'Operations', 'Tech', 'Tech']
})

# Sort DataFrame by 'Salary' in ascending order
# This sorts the DataFrame by the 'Salary' column in ascending order.
print("Ascending order by Salary:")
print(data.sort_values(by='Salary'))

# Sort DataFrame by 'Salary' in ascending order (explicitly mentioned)
# This explicitly sorts the DataFrame by the 'Salary' column in ascending order.
print("\nAscending order by Salary (explicit):")
print(data.sort_values(by='Salary', ascending=True))

# Sort DataFrame by 'Salary' in descending order
# This sorts the DataFrame by the 'Salary' column in descending order.
print("\nDescending order by Salary:")
print(data.sort_values(by='Salary', ascending=False))

# Group by 'Department' and count the number of names in each department
# This groups the data by the 'Department' column and counts the number of names in each department.
print("\nCount of Names in each Department:")
print(data.groupby("Department")["Name"].count())

# Group by 'Department' and calculate the mean salary in each department
# This groups the data by the 'Department' column and calculates the mean salary in each department.
print("\nMean Salary in each Department:")
print(data.groupby("Department")["Salary"].mean())

# Group by 'Department' and calculate the minimum salary in each department
# This groups the data by the 'Department' column and calculates the minimum salary in each department.
print("\nMinimum Salary in each Department:")
print(data.groupby("Department")["Salary"].min())

# Group by 'Department' and calculate the maximum salary in each department
# This groups the data by the 'Department' column and calculates the maximum salary in each department.
print("\nMaximum Salary in each Department:")
print(data.groupby("Department")["Salary"].max())

# Group by 'Department' and calculate the mean age in each department
# This groups the data by the 'Department' column and calculates the mean age in each department.
print("\nMean Age in each Department:")
print(data.groupby("Department")["Age"].mean())

# Filter data where 'Salary' is greater than 100000
# This filters the DataFrame to show only the rows where the 'Salary' column is greater than 100000.
print("\nEmployees with Salary greater than 100000:")
print(data[data["Salary"] > 100000])

# Filter data where 'Salary' is between 100000 and 200000
# This filters the DataFrame to show only the rows where the 'Salary' column is between 100000 and 200000.
print("\nEmployees with Salary between 100000 and 200000:")
print(data[(data["Salary"] > 100000) & (data["Salary"] < 200000)])

# Filter data where 'Age' is either 20 or 65
# This filters the DataFrame to show only the rows where the 'Age' column is either 20 or 65.
print("\nEmployees with Age either 20 or 65:")
print(data[data["Age"].isin([20, 65])])

