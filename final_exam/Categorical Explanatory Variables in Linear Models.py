#!/usr/bin/env python
# coding: utf-8

# In[52]:


# ANOVA
import pandas as pd
import statsmodels.formula.api as smf

Income = pd.read_csv("data/Income.dat", sep="\s+")


# In[53]:


Income.head(1)


# In[54]:


fit = smf.ols(formula="income ~ C(race)", data=Income).fit()
print(fit.summary())


# In[ ]:


# In[55]:


import statsmodels.api as sm


# In[56]:


fit2 = smf.ols(formula="income ~ C(race) + education", data=Income).fit()
print(fit2.summary())


# In[58]:


sm.stats.anova_lm(fit2)


# In[59]:


sm.stats.anova_lm(fit2, typ=2)


# In[ ]:
