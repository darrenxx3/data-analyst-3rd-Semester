#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World')


# In[2]:


conda install -c anconda pandas


# In[3]:


conda install -c anaconda pandas


# In[6]:


conda install -c conda-forge scrapy


# In[5]:


conda install -c anaconda beautifulsoup4


# In[18]:


import csv

with open('D:\SEMESTER3\DATAANAYSIS\lab\week2\menu_mcd.csv','r')as menufile:
    rows=csv.reader(menufile,delimiter=',')
    for r in rows:
        print(r)


# In[19]:


#import library
import pandas as pd


# In[20]:


#import CSV FORMAT

#
menu = pd.read_csv('D:\SEMESTER3\DATAANAYSIS\lab\week2\menu_mcd.csv')
menu.head()


# In[21]:


#Show All Variable information of the dataframe
menu.info()


# In[22]:


#Show ALl basic statisctics of the dataframe

menu.describe()


# In[23]:


#Trim the previous data and select only: Category, Item, Serving Size, Carbohydrates

menu_trimmed = menu[['Category','Item','Serving Size','Calories','Carbohydrates','Cholesterol']]
menu_trimmed.head()


# In[13]:


#Export the trimmed data to Excel Format

menu_trimmed.to_excel('menu_mcd_edited.xlsx')
print('Export Successful!')


# In[24]:


#Import Excel Format from the Trimmed data

menu_new = pd.read_excel('menu_mcd_edited.xlsx')
menu_new.head()


# In[25]:


#Import data Using URL

url ="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/teleCust1000t.csv"
customer = pd.read_csv(url)
customer.head()


# In[26]:


#Basic Data Scraping

#Source:https://medium.com/analytics-vidhya/how-to-scrape-data-from-a-website-using-python-for-beginner-5c770a1fbe2d
#Import Library
from bs4 import BeautifulSoup
import requests


# In[27]:


#DEfining URL
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
#ASK hosting server to fetch URL
requests.get(url)


# In[28]:


#geting request
pages = requests.get(url)
pages.text


# In[29]:


#parsel-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text,"lxml")
soup


# In[30]:


#Using find all to collect only price of items
soup.find_all('h4', class_ ='pull-right price')


# In[ ]:




