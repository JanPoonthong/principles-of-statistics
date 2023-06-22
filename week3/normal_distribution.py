from scipy.stats import norm

x1 = norm.cdf(7, 8, 0.5)
print(x1)
x2 = 1 - norm.cdf(8, 8, 0.5)
print(x2)
x3 = norm.cdf(10, 8, 0.5) - norm.cdf(7.5, 8, 0.5)
print(x3)

print("")

x4 = norm.cdf(27, 30, 1)
print(x4)
x5 = 1 - norm.cdf(32, 30, 1)
print(x5)
x6 = norm.cdf(32, 30, 1) - norm.cdf(28, 30, 1)
print(x6)
