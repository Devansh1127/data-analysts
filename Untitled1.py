#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pp
import numpy as nn
import seaborn as ss
import matplotlib.pyplot as gg



# In[3]:


d = pp.read_csv("data_python.csv")
print(d)


# In[4]:


d.shape #print the number of rows and columns 


# In[5]:


d.isnull().sum() #null values of the data 


# In[8]:


target = d["Loan_Status"]


# In[10]:


d.duplicated().sum() #here we have the none duplicated values in the data


# In[12]:


if(d['Education'][20] == 'Graduate'):
    print("yes")
    
else:
        
        print("no") 


# In[14]:


d.iloc[31:36] # prints the data of the 31 to 35 rows 


# In[26]:


d.iloc[:5:1] #prints the data of the 


# In[27]:


# initialize variables 'a' and 'b' with 5 and 6 respectively
a = 5
b = 6

# add 'a' and 'b' and assign the result into a new variable 'c'
c = a + b
print(c)


# In[28]:


# build a function to add 2 numbers
def addition(x,y):
    return(x+ y)

# use the function 'addition' to add 'a' and 'b'
addition(5, 6)


# In[29]:


# create a list consisting of first 5 even numbers and print the list
my_list = [2,4,6,8,10]
print(my_list)


# In[30]:


# access the 3rd element of the list 'my_list'
my_list[3]


# In[31]:


# given below is a dictionary having 4 unique keys, i.e., 'name', 'age', 'gender', 'is_employed'
my_dict = {'name':'Smith',
           'age':34,
           'gender': 'Male',
           'is_employed': False}

# print 'my_dict'
print(my_dict)


# In[32]:


# access value under 'name' key from 'my_dict'
my_dict["name"]


# In[33]:


# update 'is_employed' key to True
my_dict.update({'is_employed': True})

# print the updated dictionary
print(my_dict)


# In[34]:


# use a for loop to print only even numbers from the first 20 numbers, i.e. 1-20
for i in range(1,21):
    if i % 2 == 0:
        print(i)


# In[ ]:




