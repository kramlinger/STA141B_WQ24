
# In[22]:


x = [1, 1, 2, 3, 5]
x.append([8])
y = x.pop()

print(y)
print(x)


# In[23]:


x = {'1': 1, 1: [1], 1.0: not 1}

print(x['1'])
print(x[1])


# In[26]:


try: x[range(1)] = 1
except: print("hip!")
try: x[[1]] = 1
except: print("hep!")


# In[27]:


def f(n): 
    # this function returns an 
    return lambda x, m = 2: x**n + m
g = [f(i) for i in range(2)]
h = [i(3) for i in g]

help(f)
print(h)


# In[28]:


import sys

a = sys.intern('why do pangolins dream of quiche')
x = [100**100, 'hello', 'why do pangolins dream of quiche']
y = (100**100, 'hello', a)
z = (100, 'hello', 'hello')

print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(z))


# In[29]:


a = [i for i in y]
x = [100, 'hello', a]
y = x[2]
z = x[2][0]
x[2][0] = -1.0

print(y)
print(z)


# In[30]:


x = (x**2 for x in range(3))
y = [2*y for y in x]
z = sum(x)

print(y)
print(z)


# In[31]:


x = [[x, x**2] for x in range(3)]
[e[1] for i, e in enumerate(x) if i is e[0]]


# In[32]:


import numpy as np

x = [1, 'hi']
y = np.array(x)

[a == b for a, b in zip(x, y)]


# In[33]:


x = np.matrix([[1, 2], [3, 4.0], [1, 2]])

print(x.shape)
print(x.size)
print(x.dtype)


# In[34]:


try: (x - 3) @ np.array([3, 2])
except: print('hep!')
try: x + [[1, 2.0], [3, 4], [3, 4]]
except: print('hip!')
try: x[:,0] @ [1, 2.0]
except: print('hop!')


# In[35]:


import pandas as pd

x = pd.Series([1,2,3], index = [2, 1, 0])


print(x[2])
print(x.iloc[2])
print(x.loc[2])


# In[36]:


y = pd.Series([1,2,3])
try: 
    z = y @ x
    print(z)
except: 
    print('hep!')

