
# coding: utf-8

# # Lab 1

# In[1]:


print ("Hello world")


# In[3]:


a = 3 
b = 4 
a+b


# ## demo of print below

# In[4]:


print (1)
print (a)


# ### demo of add

# In[4]:


a = 5


# 1. Item 1
# 2. Item 2
# 
# 
# JMU [website ](http://www.jmu.edu/)

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()

