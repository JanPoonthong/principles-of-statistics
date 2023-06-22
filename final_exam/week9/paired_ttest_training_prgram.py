#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:14:42 2022

@author: janpoonthong
"""

import scipy.stats as stats

alpha = 0.10

before = [67, 74, 58, 45, 78, 79, 61, 83, 70, 69]
after = [89, 75, 64, 71, 80, 82, 92, 81, 73, 75]

t_value, p_value = stats.ttest_rel(before, after)
print("T-value: ", t_value)
print("P-value: ", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
