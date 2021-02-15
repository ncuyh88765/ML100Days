#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
a=np.add(1,3)
print(a)


# In[5]:


np.sqrt(9)


# In[6]:


np.mod(9,4)


# In[8]:


a=np.array([1,2,3,4,5])
b=np.array([2,3,4,5,6])
a*b


# In[3]:


#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
#60
import numpy as np
V1 = 20000
V0 = 20
20*np.log10(V1/V0)


# In[4]:


#2.30分貝的聲壓會是50分貝的幾倍?
#公式移項過後可以得到 V1 = 10^(GdB/20)*V0
#10倍
V1_30 = 10**(30/20)*V0
V1_50 = 10**(50/20)*V0
V1_30/V1_50


# In[ ]:





# In[ ]:




