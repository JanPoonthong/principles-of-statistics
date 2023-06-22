import numpy as np
from scipy.stats import norm

mean = 5.46
n = 100
confidence = 0.95
stdev = np.sqrt(2.5)

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))

mean = 5.46
n = 100
confidence = 0.99
stdev = np.sqrt(2.5)

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))


mean = 5.46
n = 100
confidence = 0.98
stdev = np.sqrt(6.5)

z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))
