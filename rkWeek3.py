#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis


import json # library to handle JSON files
from geopy.geocoders import Nominatim
import matplotlib.cm as cm
import matplotlib.colors as colors
import folium
import urllib
from bs4 import BeautifulSoup


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'    
tables = pd.read_html(url, index_col=0, attrs={"class":"wikitable"})     
toronto_df = tables[0]
toronto_df.reset_index(inplace = True)
toronto_df.head()


# In[4]:


toronto_df.shape


# Clean the data frame
# 

# In[5]:


toronto_df = toronto_df[toronto_df.Borough != 'Not assigned']
toronto_df.reset_index(drop = True, inplace = True)
toronto_df.loc[toronto_df['Neighbourhood'] == 'Not assigned', 'Neighbourhood'] = toronto_df.loc[toronto_df['Neighbourhood'] == 'Not assigned', 'Borough']
toronto_df.head(10)


# In[6]:


toronto_df.shape


# In[7]:


# Combine Codes with more than one neighborhood
neighborhoods_df = pd.DataFrame(toronto_df.groupby('Postcode')['Neighbourhood'].apply(lambda x: ', '.join(x))).reset_index()
boroughs_df = pd.DataFrame(toronto_df.groupby('Postcode')['Borough'].apply(lambda x: x.unique()[0])).reset_index()
print (neighborhoods_df.shape, boroughs_df.shape) #Confirm each has the same number of rows

toronto_unique_df = boroughs_df.merge(right = neighborhoods_df, on = 'Postcode')
toronto_unique_df.rename(columns = {'Postcode': 'PostalCode'}, inplace = True)
toronto_unique_df


# In[8]:


print (toronto_unique_df.shape)


# Part2

# In[9]:


url = "http://cocl.us/Geospatial_data"
geo_data = pd.read_csv(url)
geo_data.head()


# In[10]:


geo_data.shape


# In[11]:


geo_data.rename(columns = {'Postal Code' : 'PostalCode'}, inplace = True)
geo_data.head()


# In[12]:


toronto_geo_df = toronto_unique_df.merge(right = geo_data, on = 'PostalCode')
toronto_geo_df


# part 3

# In[15]:


address = 'Toronto, CA'
geolocator = Nominatim(user_agent="toronto_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))


# In[18]:


map_toronto = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, borough, neighborhood in zip(toronto_geo_df['Latitude'], toronto_geo_df['Longitude'], toronto_geo_df['Borough'], toronto_geo_df['Neighbourhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


# In[ ]:





# In[ ]:





# In[ ]:




