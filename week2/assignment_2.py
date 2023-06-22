from scipy.stats import binom, poisson

# n = 10 number of student
# x = 6 find sucess value
# p = 80%
one_a = binom.pmf(6, n=10, p=0.8)
print("Question 2a =", one_a)

one_b = 1 - binom.cdf(6, 10, 0.8)
print("Question 2b =", one_b)

one_c = binom.cdf(4, 10, 0.8)
print("Question 2c =", one_c)

print("")

two_a = poisson.pmf(3, 5)
print("Question 2a =", two_a)

two_b = poisson.cdf(10, 5)
print("Question 2b =", two_b)

two_c = poisson.pmf(0, 2.5)
print("Question 2c =", two_c)
