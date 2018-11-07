
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# Logistic function implementation
def logistic_eq(r,x):
    return r*x*(1-x)


# In[ ]:


# Show the logistic function
x = np.linspace(0, 1)
plt.plot(x, logistic_eq(2, x), 'k')
plt.show()

# logistic_eq(4.0009, 0.75)


# In[ ]:


# Iterate the function for a given r
def logistic_equation_orbit(seed, r, n_iter, n_skip=0):
    print('Orbit for seed {0}, growth rate of {1}, plotting {2} iterations after skipping {3}'.format(seed, r, n_iter, n_skip))
    X_t=[]
    T=[]
    t=0
    x = seed;
    # Iterate the logistic equation, printing only if n_skip steps have been skipped
    for i in range(n_iter + n_skip):
        if i >= n_skip:
            X_t.append(x)
            T.append(t)
            t+=1
        x = logistic_eq(r,x);
    # Configure and decorate the plot
    plt.plot(T, X_t)
    plt.ylim(0, 1)
    plt.xlim(0, T[-1])
    plt.xlabel('Time t')
    plt.ylabel('X_t')
    plt.show()


# In[ ]:


logistic_equation_orbit(0.1, 3.05, 100)
logistic_equation_orbit(0.1, 3.9, 100)
logistic_equation_orbit(0.1, 3.9, 100, 1000)


# In[ ]:


# Create the bifurcation diagram
def bifurcation_diagram(seed, n_skip, n_iter, step=0.0001, r_min=0):
    print("Starting with x0 seed {0}, skip plotting first {1} iterations, then plot next {2} iterations.".format(seed, n_skip, n_iter));
    # Array of r values, the x axis of the bifurcation plot
    R = []
    # Array of x_t values, the y axis of the bifurcation plot
    X = []
    
    # Create the r values to loop. For each r value we will plot n_iter points
    r_range = np.linspace(r_min, 4, int(1/step))

    for r in r_range:
        x = seed;
        # For each r, iterate the logistic function and collect datapoint if n_skip iterations have occurred
        for i in range(n_iter+n_skip+1):
            if i >= n_skip:
                R.append(r)
                X.append(x)
                
            x = logistic_eq(r,x);
    # Plot the data    
    plt.plot(R, X, ls='', marker=',')
    plt.ylim(0, 1)
    plt.xlim(r_min, 4)
    plt.xlabel('r')
    plt.ylabel('X')
    plt.show()


# In[ ]:


bifurcation_diagram(0.2, 100, 5)
bifurcation_diagram(0.2, 100, 10)
bifurcation_diagram(0.2, 100, 10, r_min=2.8)

