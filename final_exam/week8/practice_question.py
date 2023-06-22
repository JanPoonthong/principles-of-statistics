# 1
from scipy.stats import ttest_1samp

data = [55, 85, 90, 30, 45, 65, 25, 72, 103, 35]
pop_mean = 60
alpha = 0.05
tscore, pvalue = ttest_1samp(data, pop_mean)
print("T statistics: ", tscore)
print("P value: ", pvalue)
if pvalue < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")


print()


# 2
from statsmodels.stats.proportion import proportions_ztest

count = 225
sample = 400
value = 0.40
alpha = 0.01
zscore, pvalue = proportions_ztest(count, sample, value)
print("Z statistics: ", zscore)
print("P value :", pvalue)
if pvalue < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
