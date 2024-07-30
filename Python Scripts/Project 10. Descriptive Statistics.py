import numpy as np
import pandas as pd

data = [100, 20, 5, 20, 45, -100, 46]
mean_ = np.mean(data)
print("Mean of array:", mean_)

median_ = np.median(data)
print("median of array:", median_)

from scipy import stats

mode_ = stats.mode(data)
print("Mode of array:", mode_)


variance_ = np.var(data)
print("Variance of array:", variance_)

std_ = np.std(data)
print("Standard Deviation of array:", std_)

# Loading CSV file with header
data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
print(data_csv.describe())
