#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:




# 準備數據 ... 假設我要畫一個sin波 從0~180度
# 設定要畫的的x,y數據list....
x = np.arange(0,180)
y = np.cos(x * np.pi / 180.0)

# 開始畫圖
plt.plot(x,y)
# 在這個指令之前，都還在做畫圖的動作 
# 這個指令算是 "秀圖"
plt.show() 

#畫出完整的 sin 圖形
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)

plt.plot(x, y_sin)



#畫出完整的 cos 圖形

y = np.cos(x)

 # 如果要存成圖形檔:
# 把 pyplot.show() 換成下面這行:

plt.savefig("filename.png",dpi=300,format="png")


# In[6]:


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

'''
#作業

#方法不只有一種

'''

plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)

plt.show()


# In[ ]:




