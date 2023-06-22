#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:59:57 2022

@author: janpoonthong
"""

import pandas as pd
import numpy as np

Anor = pd.read_csv("http://stat4ds.rwth-aachen.de/data/Anorexia.dat", sep="\s+")

change = Anor["before"] - Anor["after"]
Anor["change"] = change
print(Anor.loc[Anor["therapy"] == "cb"]["change"].describe())

print()

changeCB = Anor.loc[Anor["therapy"] == "cb"]["change"]
import statsmodels.stats.api as sms

print(
    f"95% confidence interval of mean difference: {sms.DescrStatsW(changeCB).tconfint_mean(alpha=0.05)}"
)


from scipy.stats import t


def t2ind_confint(y1, y2, equal_var=True, alpha=0.05):

    # y1, y2 : vectors or data frames of values for group A and B
    # returns: mean_diff: mean(A)-mean(B) (float)
    # confint: CI for mu_A - mu_B (1d ndarray)
    # conf: confidence level of the CI (float)
    # df (float)
    n1 = len(y1)
    n2 = len(y2)
    var1 = np.var(y1) * n1 / (n1 - 1)
    var2 = np.var(y2) * n2 / (n2 - 1)
    if equal_var:
        df = n1 + n2 - 2
        vardiff = (
            ((n1 - 1) * var1 + (n2 - 1) * var2)
            / (n1 + n2 - 2)
            * (1 / n1 + 1 / n2)
        )
    else:
        df = (var1 / n1 + var2 / n2) ** 2 / (
            var1**2 / (n1**2 * (n1 - 1)) + var2**2 / (n2**2 * (n2 - 1))
        )
        vardiff = var1 / n1 + var2 / n2
    se = np.sqrt(vardiff)
    qt = t.ppf(1 - alpha / 2, df)  # t quantile for 100(1-alpha)% CI
    mean_diff = np.mean(y1) - np.mean(y2)
    confint = mean_diff + np.array([-1, 1]) * qt * se
    conf = 1 - alpha
    return mean_diff, confint, conf, df


cogbehav = Anor.loc[Anor["therapy"] == "cb"]["change"]
control = Anor.loc[Anor["therapy"] == "c"]["change"]
mean_diff, confint, conf, df = t2ind_confint(
    cogbehav, control
)  # call the function above
print("mean1-mean2 =", mean_diff)  # assume equal variances
print(conf, "CI:", confint)
print("df =", df)

print()

mean_diff, confint, conf, df = t2ind_confint(
    cogbehav, control, equal_var=False
)  # permit unequal variances
print("mean1-mean2 =", mean_diff)
print(conf, "CI:", confint)
print("df =", df)
