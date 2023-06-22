data = [5, 4, 8, 7, 10, 12, 8, 2, 4, 6]

import numpy as np
import statistics as sta
from scipy.stats import t

mean = np.average(data)
stdev = np.sqrt(sta.variance(data))
n = len(data)
dof = len(data) - 1
confidence = 0.95
t_value = np.abs(t.ppf((1 - confidence) / 2, dof))

print(mean - stdev * t_value / np.sqrt(n), mean + stdev * t_value / np.sqrt(n))
