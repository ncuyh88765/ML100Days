#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[53]:


name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]


# In[58]:


students_data = {'names':('name_list','sex_list','weight_list','rank_list','myopia_list'), 'formats':('U5','U5','f8','int8','?')}
students = np.array([('小明','boy','67.5','8','True'), ('小華','boy','75.3','1','True'),('小菁','girl','50.1','5','False'),('小美','girl','45.5','4','False'),('小張','boy','80.8','7','True'),('John','boy','90.4','6','True'),('Mark','boy','78.4','2','False'),('Tom','boy','70.7','3','False')],dtype=students_data)


# In[60]:


print(students)


# In[64]:


#2.呈上題，將 array 中體重(weight)數據集取出算出全部平均體重
students=[weight_list]
students


# In[65]:


np.mean(students)


# In[75]:


#3.呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重


# In[ ]:




