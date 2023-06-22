import numpy as np
import statistics as sta
from scipy.stats import t

# a
data = [7.6, 7.5, 8.0, 6.8, 7.2, 8.4, 5.3, 7.3, 7.1, 7.6]

mean = np.average(data)
stdev = np.sqrt(sta.variance(data))
n = len(data)
dof = len(data) - 1
confidence = 0.95

t_value = np.abs(t.ppf((1 - confidence) / 2, dof))
print(mean - stdev * t_value / np.sqrt(n), mean + stdev * t_value / np.sqrt(n))


# b
data = [
    7.6,
    7.5,
    8.0,
    6.8,
    7.2,
    8.4,
    5.3,
    7.3,
    7.1,
    7.6,
    9.4,
    6.4,
    7.9,
    8.7,
    6.2,
]

mean = np.average(data)
stdev = np.sqrt(sta.variance(data))
n = len(data)
dof = len(data) - 1
confidence = 0.95

t_value = np.abs(t.ppf((1 - confidence) / 2, dof))
print(mean - stdev * t_value / np.sqrt(n), mean + stdev * t_value / np.sqrt(n))
