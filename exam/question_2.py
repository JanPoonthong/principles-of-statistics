from turtle import st
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# a
n = 9
p = 0.3
x = np.arange(0, n + 1)

prob = binom.pmf(x, n, p)
print(f"PMF Probability: {prob}")
prob = binom.cdf(x, n, p)
print(f"CDF Probability: {prob}")

binomial_pmf = binom.pmf(x, n, p)
binomial_cdf = binom.cdf(x, n, p)

# pmf
plt.plot(x, binomial_pmf, color="blue")
plt.title(f"Binomial Distribution PMF (n={n}, p={p})")
plt.show()

# cdf
plt.plot(x, binomial_cdf, color="red")
plt.title(f"Binomial Distribution CDF (n={n}, p={p})")
plt.show()


# b
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

mean = 9
stdev = 3
x = np.arange(mean - 3 * stdev, mean + 3 * stdev)

prob = norm.cdf(x, mean, stdev)
print(f"CDF Probability: {prob}")

prob = norm.pdf(x, mean, stdev)
print(f"PDF Probability: {prob}")

norm_cdf = norm.cdf(x, mean, stdev)
norm_pdf = norm.pdf(x, mean, stdev)

plt.plot(x, norm_cdf, color="blue")
plt.title(f"Normal Distribution CDF (n={n}, p={p})")
plt.show()

plt.plot(x, norm_pdf, color="red")
plt.title(f"Normal Distribution PDF (n={n}, p={p})")
plt.show()
