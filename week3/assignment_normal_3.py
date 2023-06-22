from scipy.stats import norm

one_a = norm.cdf(190, 185, 2.5) - norm.cdf(180, 185, 2.5)
print(one_a)

one_b = 1 - norm.cdf(192, 185, 2.5)
print(one_b)

one_c = norm.cdf(178, 185, 2.5)
print(one_c)

print("")

two_a = 1 - norm.cdf(110, 100, 16)
print(two_a)

two_b = norm.cdf(85, 100, 16)
print(two_b)

two_c = norm.cdf(115, 100, 16) - norm.cdf(90, 100, 16)
print(two_c)
