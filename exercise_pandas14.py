#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[7]:


index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
df = pd.DataFrame(data, index=index, columns=columns)
df


# In[8]:


df.stack()
#會由最外層欄位開始轉換.原欄位為subject,type.會先由type轉換過去索引


# In[10]:


df.unstack()


# In[11]:


df = pd.DataFrame({'Name':{0:'John', 1:'Bob', 2:'Shiela'}, 
                   'Course':{0:'Masters', 1:'Graduate', 2:'Graduate'}, 
                   'Age':{0:27, 1:23, 2:21}}) 
df


# In[12]:


#只轉換Name欄位
df.melt(id_vars='Name')


# In[13]:


#id_vars:不需要被轉換的列名
#value_vars:需要轉換的列名


# In[14]:


df = pd.DataFrame({'fff': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bbb': ['P', 'Q', 'R', 'P', 'Q', 'R'],
                   'baa': [2, 3, 4, 5, 6, 7],
                   'zzz': ['h', 'i', 'j', 'k', 'l', 'm']})
df


# In[15]:


#.pivot()函數根據給定的索引/列值重新組織給定的DataFrame
#參數
#index : 新資料的索引名稱
#columns: 新資料的欄位名稱
#values :新資料的值名稱

df.pivot(index='fff', columns='bbb', values='baa')


# In[ ]:




