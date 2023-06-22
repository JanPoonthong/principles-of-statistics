import numpy as np
from scipy.stats import norm

# First question
mean = 79
n = 50
confidence = 0.95
stdev = np.sqrt(54.50)

# find the value of Z lamda
z_crit = np.abs(norm.ppf((1 - confidence) / 2))

print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))

# Second quesiton

mean = 82
n = 100
stdev = np.sqrt(6.5)
confidence = 0.90

z_crit = np.abs(norm.ppf((1 - confidence) / 2))
print((mean - stdev * z_crit / np.sqrt(n), mean + stdev * z_crit / np.sqrt(n)))
