#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
from scipy.stats import t
from matplotlib import pyplot as plt

fig, ax = plt.subplots(1, 1)


# In[34]:


df = np.array([1, 3, 8, 30])  # degrees of freedom
y = np.linspace(-4, 4, 100)


def t_pdfs():  # function that creates plot as in Figure 4.5
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    for i in range(4):
        ax.plot(y, t.pdf(y, df[i]), lw=2, linestyle="dashed")
        ax.legend(
            ["df=1", "df=3", "df=8", "df=30", "normal"], loc="upper right"
        )


t_pdfs()  # runs the function
plt.xlabel("y")
plt.ylabel("Probability density function")


# In[35]:


df = np.array([1, 10, 30, 100, 1000, 10000])
t.ppf(0.975, df)  # 0.975-quantiles for corresponding df


# In[36]:


t.cdf(1.960201, 10000)  # cumulative prob. at t=1.960201 when df=10000
