
# coding: utf-8

# In[1]:


p = range(1, 301)
def find_position(y):
    if y in p:
        return p.index(y)
    else:
        return "not in list"


# In[2]:


find_position(45)


# In[3]:


find_position(777)

