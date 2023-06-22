from scipy.stats import norm, uniform
import numpy as np
import matplotlib.pyplot as plt

mean = 0
variance = 4
stdev = np.sqrt(variance)

prob = 1 - norm.cdf(2, mean, stdev)
print(prob)

prob = norm.pdf(2, mean, stdev)
print(prob)

x = np.arange(-10, 10)

norm_cdf = norm.cdf(x, mean, stdev)
norm_pdf = norm.pdf(x, mean, stdev)

plt.plot(x, norm_cdf, color="blue")
plt.show()

plt.plot(x, norm_pdf, color="red")
plt.show()


mean = 2
stdev = 5
prob = norm.cdf(4, mean, stdev)
print(prob)

prob = norm.pdf(4, mean, stdev)
print(prob)

x = np.arange(-10, 10)

norm_cdf = norm.cdf(x, mean, stdev)
norm_pdf = norm.pdf(x, mean, stdev)

plt.plot(x, norm_cdf, color="blue")
plt.show()

plt.plot(x, norm_pdf, color="red")
plt.show()
