from scipy.stats import skewnorm
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import MinMaxScaler

import seaborn as sns
import matplotlib.pyplot as plt

num_data_points = 100
max_value = 1000
skewness = 15  # Positive values are right-skewed

skewed_random_data = skewnorm.rvs(
    a=skewness, loc=max_value, size=num_data_points, random_state=1
)
a = skewnorm.rvs(a=15, size=100, loc=max_value)
print(a)
skewed_data_scaled = MinMaxScaler().fit_transform(a.reshape(-1, 1))

# Plot the data (population) distribution
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Data Distribution", fontsize=24, fontweight="bold")

sns.histplot(
    skewed_data_scaled, bins=30, stat="density", kde=True, legend=False, ax=ax
)

# sns.histplot(skewed_data_scaled, bins=30, stat="density", kde=True, legend=False, ax=ax)
plt.show()

import numpy as np
import random

sample_size = 50
sample_mean = []
random.seed(1)  # Setting the seed for reproducibility of the result
for _ in range(2000):
    sample = random.sample(skewed_data_scaled.tolist(), 50)
    sample_mean.append(np.mean(sample))

print(f"Mean: {np.mean(sample_mean)} \n")
print(f"Median: {np.median(sample_mean)}")
print(f"Variance: {np.var(sample_mean)}")
print(f"Shew: {skew(sample_mean)}")
print(f"Kurtosis: {kurtosis(sample_mean)}")

# Plot the sampling distribution
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Sampling Distribution", fontsize=24, fontweight="bold")

# sns.histplot(sample_mean, bins=30, stat="density", kde=True, legend=False)
# plt.show()
