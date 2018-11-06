
# coding: utf-8

# In[15]:


# Logistic function implementation
def logis(r,x):
    return r*x*(1-x)


# In[20]:


# Iterate the function for a given r
# Return an array of results
def logis_map(seed, r, n_iter, n_skip=0):
    values = []
    x = logis(r,seed);
    for i in range(n_iter+n_skip-1):
        x = logis(r,x);
        if i >= n_skip:
            values.append(x);
    return values


# In[21]:


v=logis_map(0.2, 3.05, 10, 1000)
print(v)

