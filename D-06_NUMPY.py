#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])


# In[5]:


with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1, array2)


# In[7]:


npzfile=np.load('multi_array.npz')
type(npzfile)


# In[8]:


npzfile


# In[14]:


print(npzfile['array1'])
print(npzfile['array2'])


# In[23]:


np.savetxt('multi_array', '1D array' , fmt='%.18e', delimiter=' ', newline='n', header='', footer='', comments='# ', encoding=None)


# In[ ]:





# In[ ]:




