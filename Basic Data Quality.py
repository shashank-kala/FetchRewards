#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd;


# In[8]:


#Read Receipts Json File
df = pd.read_json('receipts.json',lines = True)


# In[9]:


#Check for values in the head, Gives an overall look and feel of the data
df.head()


# In[12]:


df.count()


# In[14]:


#Checking for the column name we can see it consists of multiple values 
df.rewardsReceiptStatus.unique()


# In[18]:


# Check data type of CreateDate field , it contains object type ; Relational Model will contain Date type in the different fields
df.createDate.dtypes


# In[19]:


# Th
df.userId.unique()


# In[ ]:




