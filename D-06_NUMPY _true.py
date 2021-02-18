#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])


# In[24]:


#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
np.savez('array.npz',array1,array2)


# In[25]:


#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
load_array = np.load('array.npz')
array3 = np.array([[4,5,6],[1,2,3]])
np.savez('new_array.npz',load_array['arr_0'],load_array['arr_1'],array3)


# In[ ]:




