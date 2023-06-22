import numpy as np
import math
import matplotlib.pyplot as plt

# a
ran = list(range(1, 6, 2))
data = np.random.choice(ran, 100)
weights = np.random.choice(ran, 100)


def weighted_avg_and_std(data, weights):
    average = np.average(data, weights=weights)
    variance = np.average((data - average) ** 2, weights=weights)
    return (average, math.sqrt(variance), variance)


average, stdev, variance = weighted_avg_and_std(data, weights)

print(f"Weighted Mean: {average}")
plt.hist(average)
plt.title(f"Weighted Mean: {average}")
plt.show()

print(f"Weighted variance: {variance}")
plt.hist(variance)
plt.title(f"Weighted variance: {variance}")
plt.show()

skewness = np.average((data - average) ** 3, weights=weights) / variance**1.5
print(f"Weighted skewness: {skewness}")
plt.hist(skewness)
plt.title(f"Weighted skewness: {skewness}")
plt.show()

kurtosis = np.average((data - average) ** 4, weights=weights) / variance**2
print(f"Weighted kurtosis: {kurtosis}")
plt.hist(kurtosis)
plt.title(f"Weighted kurtosis: {kurtosis}")
plt.show()

# b
def weighted_percentile(data, percents, weight=None):
    ind = np.argsort(data)
    d = data[ind]
    w = weight[ind]
    p = 1 * w.cumsum() / w.sum() * 100
    y = np.interp(percents, p, d)
    return y


first_quantile = weighted_percentile(
    np.array(data), 25, weight=np.array(weights)
)
second_quantile = weighted_percentile(
    np.array(data), 50, weight=np.array(weights)
)
third_quantile = weighted_percentile(
    np.array(data), 75, weight=np.array(weights)
)
IQR = third_quantile - first_quantile
print(
    f"First Quantile: {first_quantile}, Second Quantile: {second_quantile} Third Quantile: {third_quantile}, IOR: {IQR}"
)

# this is for normal distribution mean = 9, stdev = 3
mean = 9
stdev = 3
IQR = (mean + stdev) - (mean - stdev)
print(f"First Quantile: {mean - stdev}")
print(f"Third Quantile: {mean + stdev}")
print(f"IQR: {IQR}")
