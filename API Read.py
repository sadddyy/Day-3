#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
import json


# In[21]:


url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_jurpAFGo7IDRsQ3FzdlmU7aw0WEoXkrPm90QQjfK"


# In[22]:


response=requests.get(url)


# In[29]:


dict_a=response.json()


# In[30]:


dict_a


# In[31]:


print(type(dict_a))


# In[ ]:




