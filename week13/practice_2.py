#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:43:31 2022

@author: janpoonthong
"""


import pandas as pd
import statsmodels.formula.api as smf

Income = pd.read_csv("http://stat4ds.rwth-aachen.de/data/Income.dat", sep="\s+")
fit = smf.ols(formula="income ~ C(race)", data=Income).fit()
print(fit.summary())

import statsmodels.api as sm

aov_table = sm.stats.anova_lm(fit)  # ANOVA table
print(aov_table)

import statsmodels.stats.multicomp as mc

comp = mc.MultiComparison(Income["income"], Income["race"])
post_hoc_res = comp.tukeyhsd()
print(post_hoc_res.summary())
