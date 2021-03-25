#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#設定資料
#宣告一個 sin 正弦波
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
#設定圖樣
sns.set_style("ticks")
#繪圖
sinplot()


# In[4]:


sns.set(style="darkgrid")


# In[5]:


# 載入數據集
tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")


# In[6]:


#觀看資料集有哪些變數
tips.head()


# In[7]:


#套用x/y變數
#rleplot 關聯式繪圖 初始設定使用點圖
sns.relplot(x="total_bill",y="tip",data=tips);


# In[9]:


#設定第三個變數對點進行著色
#hue： 在同一維度上，用顏色區分不同數據
#style： 在同一維度上， 用線的不同表現形式區分， 如 點線， 虛線等


sns.relplot(x="total_bill",y="tip",hue="smoker",style="time",data=tips);


# In[11]:


#使用回歸
#regplot,regression plot 參數的定義和replot相同
sns.regplot(x="total_bill",y="tip",data=tips);


# In[13]:


sns.relplot(x="total_bill", y="tip", hue="sex", style="time",data=tips);


# In[14]:


fmri.head()


# In[16]:


sns.relplot(x="timepoint", y="signal", hue="event", style="region",data=fmri);


# In[17]:


sns.regplot(x="timepoint",y="signal",data=fmri);


# In[ ]:




