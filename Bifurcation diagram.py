
# coding: utf-8

# In[9]:


# Logistic function implementation
def logis(r,x):
    return r*x*(1-x)


# In[10]:


# Iterate the function for a given r
# Allow to skip steps
def logis_map(seed, r, n_iter, n_skip=0):
    x = logis(r,seed);
    for i in range(n_iter+n_skip-1):
        x = logis(r,x);
        if i >= n_skip:
            print(x)


# In[12]:


logis_map(0.2, 3.05, 10, 1000)


# In[14]:


import sys
sys.version
sys.version_info

