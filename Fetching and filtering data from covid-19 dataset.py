#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as n
from matplotlib import pyplot as pl
import pandas as pd


# In[3]:


df1 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data26.csv")
df2 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data27.csv")
df3 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data28.csv")
df4 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data29.csv")
df5 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data30.csv")
df6 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data31.csv")
df7 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data32.csv")
df8 = pd.read_csv("https://data.covid19india.org/csv/latest/raw_data33.csv")
# upto 12 september


# In[4]:


df1.info()


# In[9]:


df8.columns


# In[16]:


df3.columns


# In[17]:


df5 = df5.rename(columns = {"Unnamed: 5":"Detected City"})
df6 = df6.rename(columns = {"Unnamed: 5":"Detected City"})
df7 = df7.rename(columns = {"Unnamed: 5":"Detected City"})
df8 = df8.rename(columns = {"Unnamed: 5":"Detected City"})


# In[18]:


df5.columns


# In[20]:


# retain necessary column 
df1=df1.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df2=df2.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df3=df3.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df4=df4.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df5=df5.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df6=df6.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df7=df7.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]
df8=df8.loc[:,['Num Cases','Date Announced', 'Age Bracket','Gender', 'Detected City', 'Detected District', 'Detected State','Current Status']]


# In[21]:


# merge all the dataframe into one 
df = df1.append([df2,df3,df4,df5,df6,df7,df8])
df


# In[26]:


Date = df['Date Announced'].str.split('/',expand = True)
Date.columns = ['Date','Month','Year']
Date


# In[27]:


# Add 3 columns
df = pd.concat([df,Date], axis =1)
df


# In[29]:


df.to_csv("covid19india.csv")


# In[ ]:




