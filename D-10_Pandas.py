#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


stock=pd.read_csv('STOCK_DAY_0050_202009.CSV')
stock


# In[5]:


stock2=pd.read_csv('STOCK_DAY_0050_202010.CSV')                
stock2


# In[10]:


stock_data=pd.concat([stock,stock2],axis=0) 
#AXIS=0以欄標籤對齊
stock_data


# In[11]:


stock_data.loc[stock_data.open<stock_data.close]


# In[ ]:




