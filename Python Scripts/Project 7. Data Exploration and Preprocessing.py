# Importing necessary libraries
# pandas is used for data manipulation and analysis
# sqlite3 is used for interacting with SQLite databases
import pandas as pd
import sqlite3

# Loading CSV file with header
# pd.read_csv function reads a CSV file into a DataFrame
# "percent-bachelors-degrees-women-usa.csv" is the name of the CSV file being read
data_cvs =pd.read_csv("percent-bachelors-degrees-women-usa.csv")
#print(data_cvs)

# Viewing the first 100 rows of the DataFrame
print(data_cvs.head(100))

# Viewing the last 20 rows of the DataFrame
print(data_cvs.tail(20))

# Getting a concise summary of the DataFrame
# This includes the number of non-null entries and data types of each column
print(data_cvs.info())

# Handling missing values

# Removing rows with any missing values
print(data_cvs.dropna())

# Replacing missing values with the string "NULL"
print(data_cvs.fillna("NULL"))

print(data_cvs)
# Removing duplicate rows from the DataFrame
print(data_cvs.drop_duplicates())

print(data_cvs.iloc[10])

data = pd.DataFrame({'A1': [1, 2, 3],
                     'A2': [4, 5, 6],
                     'A3': [7, 8, 9]},
                    index=['X', 'Y', 'Z'])
print(data)

print(data.loc["X"])
