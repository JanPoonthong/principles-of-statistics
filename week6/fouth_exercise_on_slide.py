import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R: {r}")

print()

x = np.array([252, 244, 241, 234, 230, 223])
y = np.array([2, 2.20, 2.40, 2.60, 2.80, 3])
d = stats.pearsonr(x, y)
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R: {r}")

print(f"Correlation: {d}")

sns.scatterplot(x, y)
sns.regplot(x, y)
plt.show()
