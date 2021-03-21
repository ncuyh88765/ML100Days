#!/usr/bin/env python
# coding: utf-8

# In[1]:


#載入 numpy, 提供亂數資料與數學式, 
import numpy as np
# 載入 matplotlib
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 設定雙格畫板大小
#(a,b,c)
#a:代表x軸的分割 b:代表y軸的分割 c:代表子版的編號數
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title("Sine")

# 設定雙格畫板大小
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cosine")

plt.show()


# In[2]:


# 從 `sklearn` 載入 `datasets`
from sklearn import datasets
# 載入 matplotlib
import matplotlib.pyplot as plt

# 載入 `digits`
digits = datasets.load_digits()

# 設定圖形的大小（寬, 高）
fig = plt.figure(figsize=(4, 2))

# 調整子圖形 
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# 把前 8 個手寫數字顯示在子圖形
for i in range(8):
    # 在 2 x 4 網格中第 i + 1 個位置繪製子圖形，並且關掉座標軸刻度
    ax = fig.add_subplot(2, 4, i + 1, xticks = [], yticks = [])
    # 顯示圖形，色彩選擇灰階
    ax.imshow(digits.images[i], cmap = plt.cm.binary)
    # 在左下角標示目標值
    ax.text(0, 7, str(digits.target[i]))

# 顯示圖形
plt.show()


# In[3]:


#import matplotlib.pyplot as plt

#決定最外框
#每一個subplots就是一個axes
#題目plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)
#(0.5,0.5)代表x,y座標
#ha='center',va='center' 代表水平對齊,垂直對齊
#size文字大小 , alpha透明度

plt.axes([0.1,0.1,.8,.8])

plt.xticks([]), plt.yticks([])
plt.text(0.6,0.6, 'axes([0.1,0.1,.8,.8])',ha='center',va='center',size=20,alpha=.5)
#

#決定內框
plt.axes([0.2,0.2,.3,.3])
plt.xticks([]), plt.yticks([])
plt.text(0.5,0.5, 'axes([0.2,0.2,.3,.3])',ha='center',va='center',size=16,alpha=.5)

plt.show()


# In[4]:


#導入必要的模組
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 創建一個3d坐標系
fig = plt.figure()
ax = Axes3D(fig)
#直接查詢參數與設定
#help(plt.plot)
#help(np.random.sample)

# 利用x軸和y軸繪製sin曲線
x = np.linspace(0, 1, 100) # linspace創建等差陣列
y = np.cos(x * 2 * np.pi) / 2 + 0.5
# 通過zdir = 'z' 將資料繪製在z軸，zs = 0.5 則是將資料繪製在z = 0.5的地方
ax.plot(x, y, zs = 0.5, zdir = 'z', color = 'black', label = 'curve in (x, y)')


# In[55]:


#導入必要的模組
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure();ax=fig.add_subplot(1,1,1)


# In[56]:


ax.plot(np.random.randn(1000).cumsum(),'k',label='one')


# In[57]:


ax.plot(np.random.randn(1000).cumsum(),'k--',label='two')


# In[50]:


ax.plot(np.random.randn(1000).cumsum(),'k.',label='three')


# In[58]:


ax.legend(loc='best')


# In[52]:


ax.plot(x,y,color='blue',label='one,two,three')


# In[60]:


plt.show()


# In[ ]:





# In[ ]:




