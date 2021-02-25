#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


boston_data=pd.read_csv('boston (2).csv')
boston_data


# In[5]:


df=boston_data
print(df)
df.boxplot()
#tax欄位中位數在300-400間


# In[8]:


df2=boston_data
print(df2)
df.plot.scatter(x='NOX',y='DIS')


# In[ ]:




