from scipy.stats import uniform

one_a = uniform.cdf(6, 2, 6)
print(one_a)

one_b = uniform.cdf(8 - 5.5, 2, 6)
print(one_b)

one_c = uniform.cdf(7, 2, 6) - uniform.cdf(3, 2, 6)
print(one_c)

two_a = uniform.cdf(30, 20, 40)
print(two_a)

two_b = uniform.cdf(40, 20, 40)
print(two_b)

two_c = uniform.cdf(45, 20, 40) - uniform.cdf(35, 20, 40)
print(two_c)
