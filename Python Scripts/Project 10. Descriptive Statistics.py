# Importing necessary libraries
import numpy as np  # NumPy is used for numerical operations on arrays
import pandas as pd  # Pandas is used for data manipulation and analysis

# Creating a list of numerical data
data = [100, 20, 5, 20, 45, -100, 46]

# Calculating the mean (average) of the data
mean_ = np.mean(data)
print("Mean of array:", mean_)
# Mean provides the central value of the data set.

# Calculating the median of the data
median_ = np.median(data)
print("Median of array:", median_)
# Median is the middle value that separates the higher half from the lower half of the data set.

# Importing the stats module from the SciPy library
from scipy import stats

# Calculating the mode of the data
mode_ = stats.mode(data)
print("Mode of array:", mode_)
# Mode is the value that appears most frequently in the data set.

# Calculating the variance of the data
variance_ = np.var(data)
print("Variance of array:", variance_)
# Variance measures how far the data points are spread out from the mean.

# Calculating the standard deviation of the data
std_ = np.std(data)
print("Standard Deviation of array:", std_)
# Standard deviation is a measure of the amount of variation or dispersion of a set of values.

# Loading a CSV file into a Pandas DataFrame
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
print(data_csv.describe())
# The 'describe' method provides descriptive statistics of the DataFrame,
# such as count, mean, std (standard deviation), min, max, and percentiles.
