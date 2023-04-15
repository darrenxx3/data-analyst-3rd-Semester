#!/usr/bin/env python
# coding: utf-8

# In[1]:


#EXERCISE KELOMPOK 3
import csv
with open('D:\SEMESTER3\DATAANAYSIS\lab\week2\School_Learning_Modalities.csv','r')as menufile:
    rows=csv.reader(menufile,delimiter=',')
    for Rows in rows:
        print(Rows)


# In[2]:


#import library 
import pandas as pd


# In[3]:


#import CSV format

menu = pd.read_csv('D:\SEMESTER3\DATAANAYSIS\lab\week2\School_Learning_Modalities.csv')
menu.head()


# In[4]:


#show variable
menu.info()


# In[5]:


#show basic statistic 
menu.describe()


# In[6]:


#summary#
##sumber referensi datanya dari : https://healthdata.gov/National/School-Learning-Modalities/aitj-yx37/data##
##datanya diambil dari tahun 2021-2022 di AS, dan dibuat oleh  National Center for Educational Statistics (NCES) for SY 2020-21.
##penjelasan singkat: data ini untuk melihat estimasi kemodalan sekolah memfasilitas anak di US, secara garis besar di 
##dlm tabel tersebut dibagi menjadi 3 bagian yakni In-Person,Remote, Hybrid


# In[ ]:




