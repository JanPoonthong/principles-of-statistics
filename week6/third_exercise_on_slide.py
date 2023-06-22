import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import numpy as np

x = np.array([3.6, 2.0, 3.4, 2.8, 2.9, 3.3, 4.1, 2.5, 3.2, 3.5])
y = np.array([23, 11, 20, 17, 15, 21, 24, 13, 19, 25])

# y => p value
r = scipy.stats.pearsonr(x, y)
print(r)

sns.scatterplot(x, y)
sns.regplot(x, y)

plt.show()
