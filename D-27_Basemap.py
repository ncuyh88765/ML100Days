#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install geos')
get_ipython().system('pip install pyproj')


# In[4]:


get_ipython().system('pip install basemap')


# In[3]:


# 導入開發套件
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 新建地圖
map = Basemap() #Basemap有很多屬性，這里全都使用默認参數

# 畫圖
map.drawcoastlines()

# 顯示结果
plt.show()


# In[ ]:




