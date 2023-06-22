#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

Happy = pd.read_csv("http://stat4ds.rwth-aachen.de/data/Happy.dat", sep="\s+")
rowlabel = ["Married", "Divorced/Separated", "Never married"]
collabel = ["Very happy", "Pretty happy", "Not too happy"]

table = pd.crosstab(Happy["marital"], Happy["happiness"], margins=False)
table.index = rowlabel
table.columns = collabel
table


# In[5]:


# conditional distributions on happiness (proportions within rows):
proptable = pd.crosstab(Happy["marital"], Happy["happiness"], normalize="index")
proptable.index = rowlabel
proptable.columns = collabel
proptable


# In[6]:


import statsmodels.api as sm  # expected frequencies under H0: independence

table = sm.stats.Table(table)
print(table.fittedvalues)


# In[7]:


X2 = table.test_nominal_association()  # chi-squared test of independence
print(X2)


# In[8]:


table.standardized_resids


# In[10]:


Happy.loc[Happy["happiness"] == 1, "happiness"] = "Very"
Happy.loc[Happy["happiness"] == 2, "happiness"] = "Pretty"
Happy.loc[Happy["happiness"] == 3, "happiness"] = "Not too"
Happy.loc[Happy["marital"] == 1, "marital"] = "Married"
Happy.loc[Happy["marital"] == 2, "marital"] = "Div/Sep"
Happy.loc[Happy["marital"] == 3, "marital"] = "Never"

from statsmodels.graphics.mosaicplot import mosaic

fig, _ = mosaic(Happy, ["marital", "happiness"], statistic=True)
