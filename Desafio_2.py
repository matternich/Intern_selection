
# coding: utf-8

# In[1]:


from random import randint
import numpy


# In[3]:


p = [randint(0, 5000000) for x in range(500)]
q = [randint(0, 5000000) for x in range(50000)]

sp = set(p)
sq = set(q)
c = sp.intersection(sq)

print (c)

