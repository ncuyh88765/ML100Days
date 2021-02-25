#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[10]:


score_df = pd.DataFrame([[1,56,66,70], [2,90,45,34], [3,45,32,55], [4,70,77,89], [5,56,80,70],
                         [6,60,54,55], [7,45,70,79], [8,34,77,76], [9,25,87,60], [10,88,40,43]],
                        columns=['student_id','math_score','english_score','chinese_score'])
score_df = score_df.set_index('student_id')
score_df


# In[15]:


#a.6 號學生(student_id=6) 3 科平均分數為何？
a=score_df.mean(axis=1)
a
#6號學生平均56.33


# In[16]:


#b.6 號學生 3 科平均分數是否有贏過班上一半的同學？
a.mean()
#no


# In[21]:


#c.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
#各科開根號乘以十
b=score_df.apply(lambda x : x**(0.5)*10)
b


# In[23]:


b.mean(axis=0)


# In[ ]:




