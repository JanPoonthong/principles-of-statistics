#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:27:07 2022

@author: janpoonthong
"""

import numpy as np
from statsmodels.stats.proportion import proportions_ztest

alpha = 0.05
success_a, size_a = (410, 500)
success_b, size_b = (370, 500)

success = np.array([success_a, success_b])
size = np.array([size_a, size_b])

stat, p_value = proportions_ztest(success, size, alternative="two-sided")

print("Z-test: ", stat)
print("P-value: ", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
