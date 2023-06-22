from scipy.stats import poisson

x1 = poisson.pmf(3, 10)
print(x1)

x2 = 1 - poisson.cdf(8, 5)
print(x2)

# --------------------------------------
three_a = 1 - poisson.cdf(4, 9)
print("Question 3a =", three_a)

three_b = poisson.pmf(5, 9)
print("Question 3b =", three_b)

three_c = poisson.cdf(4, 9 / 2)
print("Question 3c =", three_c)

four_a = 1 - poisson.cdf(2, 0.25 * 12)
print("Question 4a =", four_a)

four_b = poisson.pmf(1, 0.25 * 3)
print("Question 4b =", four_b)

four_c = poisson.cdf(3, 1.5) - poisson.cdf(2, 1.5)
print("Question 4c =", four_c)
