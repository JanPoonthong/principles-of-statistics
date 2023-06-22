#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:26:16 2022

@author: janpoonthong
"""

import pandas as pd
import statsmodels.formula.api as smf

Income = pd.read_csv("Income.dat", sep="\s+")
Income.head(1)
fit = smf.ols(formula="income ~ C(race)", data=Income).fit()
print(fit.summary())  # showing some output; F stat. tests
