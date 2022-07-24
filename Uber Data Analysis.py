#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\DELL\Desktop\resume\uber-raw-data-sep14.csv")


# In[6]:


data["Date/Time"] = data["Date/Time"].map(pd.to_datetime) 


# In[5]:


data.head()


# In[7]:


data["Day"] = data["Date/Time"].apply(lambda x: x.day)


# In[8]:


data["Weekday"] = data["Date/Time"].apply(lambda x: x.weekday())


# In[9]:


data["Hour"] = data["Date/Time"].apply(lambda x: x.hour)


# In[10]:


print(data.head())


# In[11]:


print(data.head(20))


# In[12]:


sns.set(rc={'figure.figsize':(12, 10)})
sns.distplot(data["Day"])


# In[13]:


sns.distplot(data["Hour"])


# In[14]:


sns.distplot(data["Weekday"])


# In[15]:


df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))


# In[16]:


df = df.unstack()


# In[17]:


sns.heatmap(df, annot=False)


# In[18]:


data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
figsize=(12, 8), cmap=plt.get_cmap('jet'))
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()


# In[ ]:




