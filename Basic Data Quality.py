#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd;


# In[3]:


#Read Receipts Json File
df = pd.read_json('receipts.json',lines = True)


# In[4]:


#Check for values in the head, Gives an overall look and feel of the data
df.head()


# In[5]:


df.count()


# In[6]:


#Checking for the column name we can see it consists of multiple values 
df.rewardsReceiptStatus.unique()


# In[7]:


# Check data type of CreateDate field , it contains object type ; Relational Model will contain Date type in the different fields
df.createDate.dtypes


# In[8]:


# Th
df.userId.unique()


# In[18]:


#Missing Values in the Datasets
df.isna().sum()


# In[ ]:




