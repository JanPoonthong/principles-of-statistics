import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

"""
Assume the minimart were collected the data of consumer enter to the store and it found that the average of 5 consumer enter to the store every hour. Find the probability of consumer will enter to the store at least 6 in 1 hour. Draw the pmf and cdf of poisson distribution
"""
mean = 5
prob = 1 - poisson.cdf(5, mean)
print(f"CDF: {prob}")
prob = poisson.pmf(6, mean)
print(f"PMF: {prob}")

x = np.arange(0, 20)

poisson_pmf = poisson.pmf(x, mean)

plt.plot(x, poisson_pmf, color="blue")
plt.title(f"Poisson Distribution, (mean = {mean})")
plt.show()

poisson_cdf = poisson.cdf(x, mean)

plt.plot(x, poisson_cdf, color="red")
plt.title(f"Poisson Distribution, (mean = {mean})")
plt.show()


"""
Assume the average of students submit the assignment at 4 students in each day. Find the probability of student at most 6 submit the assignment in within 1 day. Draw the pmf and cdf of poisson distribution
"""


mean = 4
prob = poisson.cdf(6, mean)
print(f"CDF: {prob}")
prob = poisson.pmf(6, mean)
print(f"PMF: {prob}")

x = np.arange(0, 20)

poisson_cdf = poisson.cdf(x, mean)
poisson_pmf = poisson.pmf(x, mean)

plt.plot(x, poisson_pmf, color="blue")
plt.title(f"Poisson Distribution, (mean = {mean})")
plt.show()

plt.plot(x, poisson_cdf, color="red")
plt.title(f"Poisson Distribution, (mean = {mean})")
plt.show()
