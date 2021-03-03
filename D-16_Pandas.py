#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[8]:


index = pd.date_range("1/1/2019", periods=20, freq='D')
s=series = pd.Series(range(20), index=index)
index


# In[9]:


#轉為周資料
s.resample('W',convention='start').asfreq()


# In[10]:


s.mean()


# In[ ]:




