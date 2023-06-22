import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

sns.scatterplot(x, y)
sns.regplot(x, y)

plt.show()
