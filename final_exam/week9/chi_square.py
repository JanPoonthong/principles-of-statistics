from scipy.stats import chi2_contingency

data = [[63, 37, 45], [26, 74, 55]]
stat, p, dof, expected = chi2_contingency(data)
alpha = 0.05
print("P value is " + str(p))

if p <= alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
