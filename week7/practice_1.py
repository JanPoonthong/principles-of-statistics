import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

y = list(range(1, 10))
randomlist = np.random.choice(y, 50)

mean = np.mean(randomlist)
median = np.median(randomlist)
mode = stats.mode(randomlist)

print(mean, median, mode)
print(randomlist)
plt.boxplot(randomlist)
plt.show()
