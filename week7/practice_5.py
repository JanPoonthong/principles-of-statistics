import numpy as np
import math

data = [3, 8, 13, 18, 23]
weights = [2, 6, 13, 17, 12]


def weighted_avg_and_std(data, weights):
    average = np.average(data, weights=weights)
    variance = np.average((data - average) ** 2, weights=weights)
    return (average, math.sqrt(variance), variance)


average, stdev, variance = weighted_avg_and_std(data, weights)

print(f"Average: {average}, Stdev: {stdev}, Variance: {variance}ß")

skewness = np.average((data - average) ** 3, weights=weights) / variance**1.5
print(f"skewness: {skewness}")

kurtosis = np.average((data - average) ** 4, weights=weights) / variance**2
print(f"kurtosis: {kurtosis}")


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
