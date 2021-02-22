#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
boston_data=pd.read_csv('boston.csv')
boston_data


# In[4]:


boston_data=pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
boston_data


# In[5]:


boston_data.to_excel('boston.xlsx')


# In[ ]:




