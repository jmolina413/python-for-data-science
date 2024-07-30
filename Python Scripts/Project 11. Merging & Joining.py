import pandas as pd  # Pandas is used for data manipulation and analysis

# Creating the first DataFrame
data1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D', 'E', 'F'],
    'value1': [1, 2, 3, 4, 5, 6]
})

# Creating the second DataFrame
data2 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F', 'G', 'H'],
    'value2': [8, 9, 10, 11, 12, 13]
})

# Printing the DataFrames
print("DataFrame 1:")
print(data1)
print("\nDataFrame 2:")
print(data2)

# Performing an inner join on 'key' column
merge_inner_join = pd.merge(data1, data2, on='key', how='inner')
print("\nInner Join Result:")
print(merge_inner_join)
# Inner join returns rows with keys present in both dataframes.

# Performing a left join on 'key' column
merge_left_join = pd.merge(data1, data2, on='key', how='left')
print("\nLeft Join Result:")
print(merge_left_join)
# Left join returns all rows from the left dataframe and matched rows from the right dataframe.

# Performing a right join on 'key' column
merge_right_join = pd.merge(data1, data2, on='key', how='right')
print("\nRight Join Result:")
print(merge_right_join)
# Right join returns all rows from the right dataframe and matched rows from the left dataframe.

# Performing a left join with indicator for anti join
merged_left = pd.merge(data1, data2, on='key', how='left', indicator=True)
merge_left_anti_join = merged_left[merged_left["_merge"] == 'left_only']
merge_left_anti_join = merge_left_anti_join.drop('_merge', axis=1)
print("\nLeft Anti Join Result:")
print(merge_left_anti_join)
# Left anti join returns rows that are present in the left dataframe but not in the right dataframe.
