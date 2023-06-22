import statistics

data = [2, 5, 7, 6, 10, 8]
mean = statistics.mean(data)
print(mean)
stdev = statistics.stdev(data)
print(stdev)

from scipy.stats import norm

x1 = 1 - norm.cdf(7, mean, stdev)
print(x1)
