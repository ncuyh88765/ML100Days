#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pandas as pd 
q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],
                    columns=['Sex','Profession'])
q_df


# In[9]:


q_df = q_df.fillna('others')
q_df


# In[10]:


#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?
#使用one-hot encoding，因為Profession欄位表示職業，職業之間沒有順序性
pf = pd.get_dummies(q_df[['Profession']])
q_df = pd.concat([q_df, pf], axis=1)
q_df


# In[ ]:




