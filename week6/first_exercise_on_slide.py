import numpy as np

x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

r = np.corrcoef(x, y)
print(r)

import scipy.stats

# y => p value
r1 = scipy.stats.pearsonr(x, y)
print(r1)

# strong because is 0.75
