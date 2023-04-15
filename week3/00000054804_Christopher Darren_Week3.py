#!/usr/bin/env python
# coding: utf-8

# In[1]:


("hello world")


# In[2]:


#Variable
x = 16
y = 4

#Addition 20
print('addition: ',x+y)

#Substraction 12
print('Substraction: ', x-y)

#Multiplication 64
print('Multiplication: ', x*y)

#Division 4
print('Division: ', x/y)

#Modulus 0?
print('Modulus: ',x%y)

#Exponent -
print('Exponent: ', x**y)

#Floor Division 4
print('Floor Division: ' ,x//y)


# In[3]:


#LIST


# In[4]:


myList = ["apple","banana","cherry"]


# In[5]:


#karena listnya indexed, list hanya bisa dilakukan dengan value yang sama:

thislist = ["apple","banana"," cherry", "apple","cherry"]
print(thislist)


# In[6]:


#List Data Type

list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9,3]
list3 = [True,False,False]


# In[7]:


list1 = ["abc",34, True, 40, "male"]
list1


# In[8]:


#list item sudah di indexed dan bisa diakses dengan index number
thislist =["apple","banana","cherry"]
print(thislist[1])


# In[9]:


# negatif indexing
# -1 merupakan item terakhir, -2 2 barang terakhir dll

thislist = ["apple","banana","cherry"]
print(thislist[-1])


# In[10]:


# Range of Indexes
# melon index5 sebagai batasnya jadi tidak diambil

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])


# In[11]:


#contoh item yang kembali dari awal , tetapi bukan include ,"kiwi":

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:4])


# In[12]:


#contoh item yang dikembalikan ke awal dari "cherry" sampai ke akhir:

thislist =["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])


# In[13]:


thislist = ["apple","banana","cherry"]
if 'apple' in thislist:
    print("Yes, 'apple' is in the fruits list")


# In[14]:


#Change list Items


# In[15]:


#Change the second Item:

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# In[16]:


#Insert 'Watermelon' sebagai index ketiga:
#untuk insert itu lebih kepada menyelipkan

thislist = ["apple","banana","cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# In[17]:


#Add List Items


# In[18]:


#menggunakan fungsi append() menambahkan index di akhir, method menambahkan append item:

thislist = ["apple", "banana","cherry"]
thislist.append("orange")
print(thislist)


# In[19]:


#memasukkan item sebagai index kedua

thislist = ["apple","banana","cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[20]:


#menambahkan element tropical ke thislist:
#fungsi extend untuk menggabungkan 2 elemen list yang berbeda

thislist =["apple", "banana","cherry"]
tropical =["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)


# In[21]:


#Remove list items


# In[22]:


#mau hapus "banana"

thislist = ["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)


# In[23]:


#mau hapus menggunakan pop() method untuk menghapus spesifik index

thislist = ["apple","banana","cherry"]
thislist.pop(1)
print(thislist)


# In[24]:


#Tuples


# In[25]:


#buat sebuah tuple

thistuple = ("apple","banana","cherry")
print(thistuple)


# In[26]:


#mengakses tuple


# In[27]:


#mengakses index dari reffering index order

thistuple = ("apple","banana","cherry")
print(thistuple[1])


# In[28]:


#negative indexing

thistuple = ("apple","banana","cherry")
print(thistuple[-1])


# In[29]:


#range dari index

thistupple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistupple[2:5])


# In[30]:


#mengembalikan index dari awal

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[:4])


# In[31]:


#mengembalikan item dari "cherry" dan sampai ke akhir:

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:])


# In[32]:


#mengganti valuesnya tupple


# In[33]:


x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# In[34]:


thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


# In[35]:


#SETS
#menyimpan multiple item dalam 1 variable


# In[36]:


thisset = {"apple","banana","cherry"}
print(thisset)


# In[37]:


# duplikat tidak diperbolehkan

thisset = {"apple","banana","cherry","apple"}
print(thisset)


# In[38]:


#Access Items


# In[39]:


thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)


# In[40]:


thisset = {"apple","banana","cherry"}
print("banana" in thisset)


# In[41]:


#Add sets


# In[42]:


thisset = {"apple","banana","cherry"}
print("banana" in thisset)


# In[43]:


#sets menggunakan update untuk menggabungkan data
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}

thisset.update(tropical)
print(thisset)


# In[44]:


#Remove items

thisset = {"apple","banana","cherry"}

thisset.remove("banana")
print(thisset)


# In[45]:


thisset = {"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)


# In[46]:


#DICTIONARY


# In[47]:


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
print(thisdict)


# In[48]:


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":194
}
print(thisdict["brand"])


# In[49]:


#Duplikasi tidak dibolehkan

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    "year":2020
}
print(thisdict)


# In[50]:


thisdict = {
    "brand": "Ford",
    "electric": False,
    "year":1964,
    "colors":["red","white","blue"]
}
print(thisdict)


# In[51]:


#Access Items


# In[52]:


thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = thisdict["model"]
x


# In[53]:


x = thisdict.get("model")
x


# In[54]:


#kata kuncinya
x= thisdict.keys()
x


# In[55]:


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year":1964
}
x = car.keys()

print(x) #sebelum perubahan
car["color"] = "white"
print(x) #setelah perubahan


# In[56]:


thisdict.values()


# In[57]:


car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
x = car.values()
print(x) #sebelum perubahan
car["year"] = 2020
print(x)


# In[58]:


#conditional statements


# In[59]:


#loops


# In[60]:


my_list = [1,2,3]


# In[61]:


#whileloops


# In[62]:


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1 #sama dengan i = i +1


# In[63]:


#for loops
for i in range(len(my_list)):
    print(my_list[i])


# In[64]:


#List for loops

for element in my_list:
    print(element)


# In[65]:


#Function


# In[66]:


def square(x):
    return x**2
def multiply(a,b):
    return a*b

#function bisa di composed
square(multiply(3,2))


# In[67]:


square(multiply(a= 3, b =2))


# In[68]:


#EXERCISE

num = ''
odd = []
even = []
while num != 0:
    num = int(input())
    if (num %2) == 1:
        odd.append(num)
    else:
        even.append(num)    
print("Odd List: ",odd)
print("Even List:",even)            


# In[ ]:





# In[69]:


1,5,7

