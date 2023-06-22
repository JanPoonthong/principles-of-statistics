#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:01:41 2022

@author: janpoonthong
"""

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

alpha = 0.10
success_a, size_a = (795, 1000)
success_b, size_b = (178, 500)

success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

stat, p_value = proportions_ztest(success, size, alternative="two-sided")

print("Z-test: ", stat)
print("P-value: ", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")


print()


alpha = 0.02
success_a, size_a = (560, 1000)
success_b, size_b = (486, 1000)

success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

stat, p_value = proportions_ztest(success, size, alternative="two-sided")

print("Z-test: ", stat)
print("P-value: ", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
