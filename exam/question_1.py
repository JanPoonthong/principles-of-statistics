# a
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

y = list(range(1, 6, 2))
randomlist = np.random.choice(y, 100)

mean = np.mean(randomlist)
median = np.median(randomlist)
mode = stats.mode(randomlist).mode

print(f"This is the mean: {mean}")
print(f"This is the median: {median}")
print(f"This is the mode: {mode}")
print()
print(f"This is random list: {randomlist}")

plt.boxplot(randomlist)
plt.title("Data")
plt.show()

plt.hist(mean)  # histogram
plt.title(f"Mean: {mean}")
plt.show()

plt.hist(median)  # histogram
plt.title(f"Median: {median}")
plt.show()

plt.hist(mode)  # histogram
plt.title(f"Mode: {mode}")
plt.show()


# b
# calculate P(A|B) given P(A), P(B|A), P(B|not A)
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    # calculate P(not A)
    not_a = 1 - p_a
    # calculate P(B)
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    # calculate P(A|B)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b


# P(A)
p_a = 3
# P(B|A)
p_b_given_a = 5
# P(B|not A)
p_b_given_not_a = 3
# calculate P(A|B)
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
# summarize
print("P(A|B) = %.3f%%" % (result * 100))
