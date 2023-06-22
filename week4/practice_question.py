import math
import numpy as np

data = [12.5, 18, 23, 28, 33, 38]
weights = [3, 15, 23, 36, 17, 9]


def weighted_avg_and_std(data, weights):
    average = np.average(data, weights=weights)
    variance = np.average((data - average) ** 2, weights=weights)
    return (average, math.sqrt(variance))


print(weighted_avg_and_std(data, weights))
