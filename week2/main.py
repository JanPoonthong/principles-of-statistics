from scipy.stats import binom

x1 = binom.pmf(1, 10, 0.7)
print(x1)


# oppsite to fid prob. at least 8 student are satis
x2 = 1 - binom.cdf(7, 10, 0.7)
print(x2)
