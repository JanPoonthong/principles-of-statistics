from statsmodels.stats.weightstats import ztest

data = [23, 26, 32, 33, 21, 29, 28, 36, 34, 41]
# Significance level
alpha = 0.05
zscore, pvalue = ztest(data, value=30)
print("Z statistics: ", zscore)
print("P value: ", pvalue)
if pvalue < alpha:
    print("Reject null hypothesis")
else:
    print("Fail to Reject null hypothesis")
