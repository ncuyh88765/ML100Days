#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得鳶尾花資料集
df = sns.load_dataset('iris')


# In[4]:


df.info()


# In[5]:


sns.boxplot(data = df, orient = "h")
#orient 設置圖的繪製方向(垂直或水平)

plt.show()


# In[6]:


#stripplot散點圖
sns.stripplot(x = "species", y = "petal_length", data = df)
plt.show()


# In[8]:


sns.stripplot(x="species",y="petal_length",data=df,jitter=True)
#jitter:true數字，當數據重和較多時 用該參數做一些調整


# In[9]:


sns.stripplot(x="petal_length",y="species",data=df)
plt.show()


# In[12]:


sns.stripplot(x="species",y="petal_length",data=df,dodge=True)
#dodge 若為true則沿著分類軸 將數據分離出來
plt.show()


# In[13]:


sns.stripplot(x="species",y="petal_length",data=df,jitter=0.5)

plt.show()


# In[14]:


df=sns.load_dataset('titanic')


# In[15]:


df.info()


# In[19]:


sns.barplot(x="sex",y="survived",data=df)


# In[21]:


df=sns.load_dataset('tips')


# In[23]:


df.info()


# In[24]:


sns.boxplot(x="day",y="total_bill",data=df)


# In[30]:


sns.stripplot(x="day",y="total_bill",data=df,jitter=0.3)
plt.show()


# In[ ]:




