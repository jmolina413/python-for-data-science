import matplotlib.pyplot as plt

# Define x and y values for the plots
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Line Plot
plt.plot(x_values, y_values, color='green')
# Creates a line plot with x_values and y_values, with the line colored green
plt.xlabel("X-axis placeholder")
# Labels the x-axis as "X-axis placeholder"
plt.ylabel("Y-axis placeholder")
# Labels the y-axis as "Y-axis placeholder"
plt.title("Title Placeholder")
# Sets the title of the plot to "Title Placeholder"
plt.show()
# Displays the plot

# Scatter Plot
plt.scatter(x_values, y_values, color='green')
# Creates a scatter plot with x_values and y_values, with points colored green
plt.xlabel("X-axis placeholder")
# Labels the x-axis as "X-axis placeholder"
plt.ylabel("Y-axis placeholder")
# Labels the y-axis as "Y-axis placeholder"
plt.title("Title Placeholder")
# Sets the title of the plot to "Title Placeholder"
plt.show()
# Displays the plot

# Bar Plot
cat = ["cat", "dog", "horse", "mouse"]
# Defines the categories for the x-axis
cat_value = [10, 30, 100, 1]
# Defines the values for the y-axis corresponding to each category
plt.bar(cat, cat_value)
# Creates a bar plot with categories as x-axis labels and cat_value as bar heights
plt.xlabel("Animals")
# Labels the x-axis as "Animals"
plt.ylabel("Weight of an Animal")
# Labels the y-axis as "Weight of an Animal"
plt.title("Weight per animal")
# Sets the title of the plot to "Weight per animal"
plt.show()
# Displays the plot

import numpy as np

# Generate random data from a normal distribution
x_normal = np.random.normal(0, 1, 100)

# Histogram of Random Data
plt.hist(x_normal, color="forestgreen")
# Creates a histogram of x_normal with bars colored forest green
plt.xlabel("X")
# Labels the x-axis as "X"
plt.ylabel("Frequency")
# Labels the y-axis as "Frequency"
plt.title("Randomly Sampled Data from Standard Normal Distribution")
# Sets the title of the plot to "Randomly Sampled Data from Standard Normal Distribution"
plt.show()
# Displays the plot

from scipy.stats import norm

# Define population distribution values
x_values = np.arange(-4, 4, 0.01)
# Creates an array of x values from -4 to 4 with a step of 0.01
y_values = norm.pdf(x_values)
# Calculates the probability density function (pdf) values for a standard normal distribution

# Generate random samples from a normal distribution
X = np.random.normal(0, 1, 1000)

# Histogram of Random Samples with Density
counts, bins, ignored = plt.hist(X, 30, density=True, color='purple', label='Sampling Distribution')
# Creates a histogram of X with 30 bins, normalized to form a probability density, bars colored purple, labeled as 'Sampling Distribution'

# Plot population distribution
plt.plot(x_values, y_values, color='y', linewidth=2.5, label='Population Distribution')
# Plots the population distribution with yellow line, linewidth of 2.5, labeled as 'Population Distribution'

# Add title and labels
plt.title("Randomly generating 1000 obs from Normal distribution mu = 0 sigma = 1")
# Sets the title of the plot
plt.ylabel("Probability")
# Labels the y-axis as "Probability"

# Add legend
plt.legend()
# Adds a legend to the plot

# Show plot
plt.show()
# Displays the plot
