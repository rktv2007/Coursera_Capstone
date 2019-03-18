#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files
import urllib
from bs4 import BeautifulSoup


# In[2]:


get_ipython().system("wget -q -O 'Canada_data.json' https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")
print('Data downloaded!')


# In[3]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# In[4]:


request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response)
                     
print(soup.prettify())


# In[5]:


soup.title.string


# In[6]:


all_tables=soup.find_all('table')


# In[23]:


right_table=soup.find('table', {"class":'wikitable sortable jquery-tablesorter'})
right_table


# In[24]:


soup.find_all('table',class_='wikitable sortable jquery-tablesorter')


# In[19]:


A=[]
B=[]
C=[]


# In[29]:


rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


# In[30]:


import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)


# In[25]:


for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    #if len(cells)==6: #Only extract table body not heading
    A.append(cells[0].find(text=True))
    B.append(states[0].find(text=True))
    C.append(cells[1].find(text=True))
        


# In[ ]:




