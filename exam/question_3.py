# a
import numpy as np

n, p = 100, 0.55
x = np.random.binomial(n, p, 1)
print(f"binomial random variable: {x}")
print(f"simulated proportion of the coin: {x/n}")


# b
import numpy as np
import matplotlib.pyplot as plt
import statistics

results = np.random.binomial(n, p, 1000) / n
mean = statistics.mean(results)
stdev = statistics.stdev(results)
print(f"Mean: {mean}")
print(f"Stdev: {stdev}")
print(f"Result: {results}")
plt.hist(results, bins=14, edgecolor="k")
plt.xlabel("Sample proportion")
plt.ylabel("Frequency")
plt.show()
