# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.stats as stats

alpha = 0.05
pre = [30, 31, 34, 40, 36, 35, 34, 30, 38, 39]
post = [30, 31, 32, 38, 32, 31, 32, 29, 28, 30]

t_value, p_value = stats.ttest_rel(pre, post)
print("T-value: ", t_value)
print("P-value: ", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
