import numpy as np
from scipy.stats import norm

mean = 42.95
stdev = np.sqrt(5)
n = 100
confidence = 0.95

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))
