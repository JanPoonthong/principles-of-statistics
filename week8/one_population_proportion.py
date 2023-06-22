from statsmodels.stats.proportion import proportions_ztest

count = 22
sample = 1000
value = 0.01
aplha = 0.1
zscore, pvalue = proportions_ztest(count, sample, value)
print("Z statistics: ", zscore)
print("P value: ", pvalue)

if pvalue < aplha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
