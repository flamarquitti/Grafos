#!/usr/bin/env python
# coding: utf-8

# In[1]:


from igraph import *
import numpy as np


# In[3]:


g1 = Graph.Erdos_Renyi(10,0.3,directed=False)
g1.vcount()


# In[5]:


g2 = Graph.Barabasi(n=12, m=33,directed=False, power=3)
g2.vcount()


# In[6]:


g = g1+g2
g.vcount()


# In[7]:


g.ecount()


# In[8]:


g.get_edgelist()


# In[64]:


g.get_edgelist()


# In[9]:


g.add_edge(1,21)


# In[10]:


g.get_edgelist()

