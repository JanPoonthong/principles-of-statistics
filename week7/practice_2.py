import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# k -> we want
# n -> trial
# p -> propability

n = 12
p = 1 / 6
x = np.arange(0, n + 1)

prob = binom.pmf(5, n, p)
print(prob)
prob = binom.cdf(5, n, p)
print(prob)

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


n = 20
p = 1 / 2
x = np.arange(0, n + 1)

prob = binom.pmf(8, n, p)
print(prob)
prob = binom.cdf(8, n, p)
print(prob)

binomial_pmf = binom.pmf(x, n, p)
binomial_cdf = binom.cdf(x, n, p)

# pmf
plt.plot(x, binomial_pmf, color="blue")
plt.title(f"binomial distribution PMF (n={n}, p={p})")
plt.show()

# cdf
plt.plot(x, binomial_cdf, color="blue")
plt.title(f"binomial distribution CDF (n={n}, p={p})")
plt.show()
