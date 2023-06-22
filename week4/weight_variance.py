import math
import numpy as np

data = [25, 30, 35, 40, 45, 50]
weights = [8, 4, 3, 4, 5, 6]


def weighted_avg_and_std(data, weights):
    average = np.average(data, weights=weights)
    variance = np.average((data - average) ** 2, weights=weights)
    return (average, math.sqrt(variance))


print(weighted_avg_and_std(data, weights))
