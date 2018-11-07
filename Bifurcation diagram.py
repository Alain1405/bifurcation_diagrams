
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


# Logistic function implementation
def logis(r,x):
    return r*x*(1-x)


# In[ ]:


# Iterate the function for a given r
def logis_map(seed, r, n_iter, n_skip=0):
    values = []
    x = logis(r,seed);
    for i in range(n_iter+n_skip-1):
        x = logis(r,x);
        if i >= n_skip:
            values.append(x);
    return values


# In[ ]:


# Test for seed of 0.2, growth rate of 3.05 returning 10 iterations after skipping 1000
print(logis_map(0.2, 3.05, 10, 1000))


# In[ ]:


# Create the bifurcation diagram
def bifurcation_diagram(seed, n_skip, n_iter, step=0.001):
    print("Starting with x0 seed {0}, skip plotting first {1} iterations, then plot next {2} iterations.".format(seed, n_skip, n_iter));
    r_range = np.linspace(0, 1, num=int(1/step))
    bif_diagram = []
    for r in r_range:
        bif_diagram.append(logis_map(seed, r, n_iter, n_skip))
    return bif_diagram


# In[ ]:


diagram = bifurcation_diagram(0.2, 10, 100)
print(diagram)

