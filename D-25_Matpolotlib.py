#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

import numpy as np 

import seaborn as sns

import matplotlib as mpl

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


# In[2]:


#如何察知工作目錄:
import os
os.getcwd()

df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")


# In[4]:


#資料整理
df_red["color"] = "R"
df_white["color"] = "W"

#整合紅酒與白酒的資料
df_all=pd.concat([df_red,df_white],axis=0)

# 檢查合併後的資料集
df_all.head()


# In[5]:


# 重新命名特徵
df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
# 檢查合併後的資料集
df_all.head()


# In[6]:


#處理缺失值
df = pd.get_dummies(df_all, columns=["color"])
df_all.isnull().sum()


# In[7]:


df_all.info()


# In[8]:


df_all.describe()


# In[9]:


#所有數值數據數值不一, 難以由圖表一眼看清
#在垂直軸上計數,在水平軸上使用值範圍。hist 函數通過將所有屬性繪製在一起使操作變得簡單。
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    

plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[13]:


# 作業(1):更改df_all.hist裡面bins的參數值, 看看資料分布的變化

df_all.hist(bins=100, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[14]:


df_all.hist(bins=100, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True)    
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[17]:


df_all.hist(bins=100, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False)    
plt.tight_layout(rect=(0, 0, 3.5, 3.5))


# In[ ]:




