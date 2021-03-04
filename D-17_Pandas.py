#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


import numpy as np
import time


# In[4]:


score_df = pd.DataFrame([[1,50,80,70,'boy',1], 
              [2,60,45,50,'boy',2],
              [3,98,43,55,'boy',1],
              [4,70,69,89,'boy',2],
              [5,56,79,60,'girl',1],
              [6,60,68,55,'girl',2],
              [7,45,70,77,'girl',1],
              [8,55,77,76,'girl',2],
              [9,25,57,60,'girl',1],
              [10,88,40,43,'girl',3],
              [11,25,60,45,'boy',3],
              [12,80,60,23,'boy',3],
              [13,20,90,66,'girl',3],
              [14,50,50,50,'girl',3],
              [15,89,67,77,'girl',3]],columns=['student_id','math_score','english_score','chinese_score','sex','class'])
score_df


# In[5]:


#agg使用Python的內建函式
star_time = time.time()
score_df.groupby('class').agg('mean')
end_time = time.time()
end_time - star_time


# In[7]:


star_time=time.time()
score_df.groupby('class').transform('mean')
end_time=time.time()
end_time-star_time


# In[10]:


score_df3=score_df.copy()
star_time=time.time()
score_df3['Pass_math']=score_df3.math_score.isin(range(60,100))
end_time=time.time()
end_time-star_time


# In[11]:


#遇到大資料集時，常有記憶體不足的問題
#首先先生成大資料，因為改善部分不同所以分成浮點數float與整數int的資料集，可以看到不管浮點數還是整數都佔了800128bytes
float_data = pd.DataFrame(np.random.uniform(0,5,100000).reshape(1000,100))
int_data = pd.DataFrame(np.random.randint(0,1000,100000).reshape(1000,100))
int_data.memory_usage(deep=True).sum(), float_data.memory_usage(deep=True).sum()


# In[12]:


#整數型態int改成uint減少記憶體正用空間，使用前800128bytes，使用後剩下200128bytes
downcast_int = int_data.apply(pd.to_numeric,downcast='unsigned')
int_data.memory_usage(deep=True).sum(),downcast_int.memory_usage(deep=True).sum()


# In[13]:


#原本有100個欄位是int64，經過downcast變成了100個欄位的uint16
compare_int = pd.concat([int_data.dtypes,downcast_int.dtypes],axis=1)
compare_int.columns = ['before','after']
compare_int.apply(pd.value_counts)


# In[14]:


#在速度較慢的時候，可以先從哪邊開始檢查？
#先從資料格式開始檢查，可已轉成pkl或者hdf格式
#或多利用python內建函式，可以提高效率


# In[ ]:


#資料過大時應採取什麼方式讓記憶體占用量下降？
#透過欄位的型態的降級有助於減少記憶體占空間

