#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#題目:
#english_score = np.array([55,89,76,65,48,70])
#math_score = np.array([60,85,60,68,np.nan,60])
#chinese_score = np.array([65,90,82,72,66,77])
#上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。

#1請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
#2第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
#3用補考後資料找出與國文成績相關係數最高的學科?


# In[1]:


import numpy as np
e=english_score = np.array([55,89,76,65,48,70])
m=math_score = np.array([60,85,60,68,np.nan,60])
c=chinese_score = np.array([65,90,82,72,66,77])


# In[25]:


#最大值
data1=np.amax(e)
data2=np.amax(m)
data3=np.amax(c)
print("英文成績最大值",data1)
print(data2)
print("國文成績最大值",data3)
#排除數學成績nan
data4=np.nanmax(m)
print("數學成績最大值",data4)


# In[26]:


#最小值
data1=np.amin(e)
data2=np.amin(m)
data3=np.amin(c)
print("英文成績最小值",data1)
print(data2)
print("國文成績最小值",data3)
#排除數學成績nan
data4=np.nanmin(m)
print("數學成績最小值",data4)


# In[27]:


#平均
data1=np.mean(e)
data2=np.mean(m)
data3=np.mean(c)
print("英文平均成績",data1)
print(data2)
print("國文平均成績",data3)
#排除數學成績nan
data4=np.nanmean(m)
print("數學平均成績",data4)


# In[29]:


#標準差
data1=np.std(e)
data2=np.std(m)
data3=np.std(c)
print("英文標準差",data1)
print(data2)
print("國文標準差",data3)
#排除數學成績nan
data4=np.nanstd(m)
print("數學標準差",data4)


# In[31]:


m=math_score = np.array([60,85,60,68,55,60])
data1=np.amax(m)
data2=np.amin(m)
data3=np.mean(m)
data4=np.std(m)
print("數學科最高分",data1)
print("數學科最低分",data2)
print("數學科平均",data3)
print("數學科標準差",data4)


# In[32]:


np.corrcoef(c,m)


# In[33]:


np.corrcoef(c,e)


# In[ ]:




