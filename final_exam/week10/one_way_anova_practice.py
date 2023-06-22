from scipy.stats import f_oneway
import matplotlib.pyplot as plt

group1 = [34, 24, 31, 29, 30, 28, 32, 26, 37, 36]
group2 = [84, 91, 78, 79, 82, 88, 85, 81, 90, 85]
group3 = [52, 54, 43, 49, 48, 55, 49, 57, 53, 55]

anova, pvalue = f_oneway(group1, group2, group3)

print("The ANOVA value is", anova)
print("The p-value is", pvalue)

alpha = 0.05
if pvalue < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")

data = [group1, group2, group3]

fig = plt.figure(figsize=(10, 7))

# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])

# Creating plot
bp = ax.boxplot(data)

# show plot
plt.show()
