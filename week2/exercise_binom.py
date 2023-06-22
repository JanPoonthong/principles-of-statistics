from scipy.stats import binom

# Question number 1
a = 1 - binom.cdf(9, 20, 0.4)
print("Question 1a =", a)

b = binom.cdf(4, 20, 0.4)
print("Question 1b =", b)

c = binom.pmf(5, 20, 0.4)
print("Question 1c =", c)

print("")
# Question number 2
a_two = 1 - binom.cdf(4, 10, 0.2)
print("Question 2a =", a_two)

b_two = binom.cdf(3, 10, 0.8)
# Teacher b_two = binom.cdf(3, 10, 0.2)
print("Question 2b =", b_two)
