from scipy.stats import uniform

x1 = 1 - uniform.cdf(4, 3, 3)
print(x1)

x2 = uniform.cdf(4.5, 3, 3)
print(x2)

print("")
x3 = 1 - uniform.cdf(135, 120, 20)
print(x3)

x4 = uniform.cdf(135, 120, 20) - uniform.cdf(125, 120, 20)
print(x4)
