data = [15, 18, 19, 20, 23, 22, 16, 25]

import numpy as np
import statistics as sta
from scipy.stats import t

mean = np.average(data)
stdev = np.sqrt(sta.variance(data))
n = len(data)
dof = len(data) - 1
confidence = 0.9
t_value = np.abs(t.ppf((1 - confidence) / 2, dof))

print(mean - stdev * t_value / np.sqrt(n), mean + stdev * t_value / np.sqrt(n))
