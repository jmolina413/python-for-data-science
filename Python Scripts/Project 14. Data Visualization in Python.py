import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#plt.plot(x_values, y_values, color = 'green')
#plt.xlabel("X-axis placeholder")
#plt.ylabel("Y-axis placeholder")
#plt.title("Title Placeholder")
#plt.show()



#plt.scatter(x_values, y_values, color = 'green')
#plt.xlabel("X-axis placeholder")
#plt.ylabel("Y-axis placeholder")
#plt.title("Title Placeholder")
#plt.show()

#cat = ["cat", "dog", "horse", "mouse"]
#cat_value = [10, 30, 100, 1]

#plt.bar(cat, cat_value)
#plt.xlabel("Animals")
#plt.ylabel("Weight of an Animal")
#plt.title("Weight per animal")
#plt.show()

import numpy as np
x_normal = np.random.normal(0, 1, 100)
plt.hist(X_normal, color = "forestgreen")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data from Standard Normal Distribution")
plt.show()

from scipy.stats import norm

# Population distribution
x_values = np.arange(-4, 4, 0.01)
y_values = norm.pdf(x_values)

# Generate random samples
X = np.random.normal(0, 1, 1000)

# Plot histogram of samples with density
counts, bins, ignored = plt.hist(X, 30, density=True, color='purple', label='Sampling Distribution')

# Plot population distribution
plt.plot(x_values, y_values, color='y', linewidth=2.5, label='Population Distribution')

# Add title and labels
plt.title("Randomly generating 1000 obs from Normal distribution mu = 0 sigma = 1")
plt.ylabel("Probability")

# Add legend
plt.legend()

# Show plot
plt.show()