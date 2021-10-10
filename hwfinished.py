#!/usr/bin/env python
# coding: utf-8

# # Data Collections 2 (Dictionaries, Sets) and Importing Modules

# In[4]:


s="Hey welcome to doing whiteboard problems get prepared to figure out a problem on the fly"
new_string = ""
def my_string(string):
    for x in string:
        print(x)
        if x.lower() == "y":
            string += x"y!"
        
            
            
            
    
    
    


# ## Tasks Today:
# 
# 1) Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring (key, value) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accessing Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #1 - Print the eye color of each person in a double nested dict <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Adding New Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Modifying Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Removing Key, Value Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Looping a Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Looping Only Keys <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Looping Only Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format()  <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) sorted() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Lists with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; k) Dictionaries with Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; l) Dictionaries with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, which prints all names and addresses after they're done putting information in...  <br>
# 2) Set <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) .add() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .union() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .intersection() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .difference() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Frozen Set <br>
# 3) Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Importing Entire Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Importing Methods Only <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Using the 'as' Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Creating a Module <br>
# 4) Exercises <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Build a Shopping Cart <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Create Your Own Module <br>

# ## Dictionary <br>
# <p>A collection of data with 'key:value' pairs. Dictionaries are ordered as of Python 3.6</p>

# ##### Declaring (key, value)

# In[1]:


# key : value pairs
# keys should be unique
# keys can use numbers or string

d = {} #Empty dictionary


# In[ ]:


d1 = {
    "Key":"Value",
    "name": "Steve", 
    0:"integer"
}
print(d1)
d = dict(key="Value,")


# ##### Accessing Values

# In[5]:


d1 = {
    "Key":"Value",
    "name": "Steve", 
    0:"integer"
}

d1["name"]


# ## In-Class Exercise #1 - Print a formatted statement from the dictionary below <br>
# <p>The output should be '2018 Chevrolet Silverado'</p>

# In[ ]:





# In[21]:


# use the dict below
#Output: I have a 2018 Chevrolet Silverado
truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}
print(f"I have a {truck['year']} {truck['make']} {truck['model']}")


# ##### Adding New Pairs

# In[23]:


truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}
print(truck.get('year'))

#truck['color']

print(truck.get("color", "red"))


# In[27]:


truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}
truck['year'] = 2020
print(truck)
    
truck['color']='Blue'
print(truck)
    
truck.update({'milage': 100000})
    
print(truck)
    


# In[ ]:





# ##### Modifying Values

# In[3]:


#dict[existing key] = new value


# ##### Removing Key, Value Pairs

# In[32]:


# del dict[key]
truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}
truck['year'] = 2020
del truck['year']
print[truck]


# ##### Looping a Dictionary

# In[43]:


# .items()
truck.items()

for key, value in truck.items():
    print('key is',key, 'and the value is:', value)
    
# a, b, c = 1, 2, 3

# print(a)
# print(b)
# print(c)


# ##### Looping Only Keys

# In[33]:


truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}# .keys()
for key in truck:
    print('the value is', key)
    print('the value is ',truck[key])


# In[ ]:





# ##### Looping Only Values

# In[46]:


# .values()
for value in truck:
    print(value)


# ## In-Class Exercise #2 - Create a Function that Prints All Key Value Pairs within an f string <br>
# <p><b>Output should be:</b><br>
# Max has blue eyes<br>
# Lilly has brown eyes<br>
# Barney has blue eyes<br>
# etc.
# </p>

# In[48]:


# use the dict below

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}
def class_ex():
    for key, value in people.items():
        print(f'{key} has {value} eyes')
        
class_ex()


# ##### sorted()

# In[9]:


# sorts variables in order
# sorted(dict.values()) or dict.keys() or dict.items()


# ##### List with Dictionaries

# In[10]:


names = ['dave', 'randy','greg', {'random_guy': 'robert', 'another_guy': 'travis'}]


# ##### Dictionaries with Lists

# In[11]:


# be careful when using numbers as keys in dictionaries, don't confuse them with indexes
d5 = {
    'students':["mark", "Natasha", "toan"]
    "age":[22, 55, 6]
}


# ##### Dictionaries with Dictionaries

# In[12]:


# to get values, must traverse through keys


# ## Using Python's Hashing Function

# In[13]:


# hash(var)


# In[57]:


my_items=[]
while True:
    response = input("what do you want to do add or remove or quit ? ")
    if response == "quit":
        break
    elif response == "add":
        item=input("what do you want to add? ").strip
        my_items.appened(item)
    elif response =="remove":
        item=("what do you want to remove? ").strip
        my_items.remove(item)
    print("your items: ", my_items)


# ## Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, and continues to do so until they choose to 'quit'. Once they quit, the program should print all names and addresses. <br>
# <p>
# <b>Proper steps:</b><br>
# step 1: write a function that takes in information and stores it in a dictionary<br>
# step 2: define an empty dictionary to work with<br>
# step 3: create our loop, which asks the user for information until they quit<br>
# step 4: ask for the information, and store it into variables<br>
# step 5: check if the user types quit<br>
# step 5a: print out all information<br>
# step 5b: break out of the loop<br>
# step 6: if they didn't quit, add the information to the dictionary<br>
# step 7: invoke the function by calling it
# </p>

# In[58]:


from IPython.display import clear_output #This module will clear all pre-exising output form your program

def user_info():
    my_dict={}
    while True:
        clear_output()
        name=input("what is your name? ").strip()
        if name.lower == "quit":
            print(my_dict)
            break
        address = input("what is your address? ").strip()
        if address.lower == "quit":
            print(my_dict)
            break
        my_dict[name]=address
    return user_info

user_info()
    
    


# ## Set <br>
# <p>A Set is an unordered collection data type that is iterable (loop), mutable, and has no duplicate elements.<br>Major advantage is that it is highly optimized in checking if something is in the set, as opposed to checking if something is in a list.</p>

# ##### Declaring

# In[15]:


# set() or {}
# no order {3, 2, 1} outputs as {1, 2, 3}


# ##### .add()

# In[16]:


# set.add()


# ##### .remove()

# In[17]:


# removes by value
# set.remove()
# nums.remove(56)


# ##### .union() 

# In[18]:


# Returns a union of two sets, can also use '|' or set.union(set)
# joins all numbers, gets rid of duplicates
set1 = {1,2,3,4}
set2 = {3,4,5,6}


# ##### .intersection()

# In[19]:


# Returns an intersection of two sets, can also use '&'
# only takes similar elements from both sets
set1 = {1,2,3,4}
set2 = {1,2,3,4}


# ##### .difference()

# In[20]:


# Returns a set containing all the elements of invoking set that are not in the second set, can also use '-'
# only takes values from the first set that are not in the second set
# order matters

set1 = {1,2,3,4}
set2 = {1,2,3,4}


# ##### .clear()

# In[21]:


# Empties the whole set
# set.clear()


# ##### Frozenset <br>
# <p>Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.</p><br><b>Unique & Immutable</b>

# In[22]:


# frozenset([])
s3 = {1,2,3,4,5,6}


# ## Modules

# ##### Importing Entire Modules

# In[63]:


from math import pi
pi


# In[61]:


# import or from 'xxx' import *
# import math
import math

print(math.pi)
print(math.floor(5/2))
print(math.ceil(5/2))


# In[ ]:





# ##### Importing Methods Only

# In[24]:


# from 'xxx' import 'xxx'
# from math import floor


# ##### Using the 'as' Keyword

# In[25]:


# from 'xxx' import 'xxx' as 'xxx' or import 'xxx' as 'xxx'
# from math import floor as f


# ##### Creating a Module

# In[70]:


from my_mod import say_hello

my_mod.say_hello("obe")


# # Exercises

# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

# In[26]:


from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

shopping_cart={}
def shopping_cart_function():
     while True:
        clear_output()
        item = input("What would you like to do show, add, remove, or quit? ")
        if item.lower() == 'quit':
            print(shopping_cart)
            break
        if item.lower() == 'add':
          item = input("what would you like to add? ")
          amount = input("how many would you like to add? ")
        if item.lower()=='quit':
            print(shopping_cart)
            break
        if item.lower() =='remove':
          item = input('what would you like to remove? ')
          del shopping_cart[item]
          print(shopping_cart)
        if item.lower == 'show':
          print(shopping_cart)
          break
        shopping_cart[item]=amount
     return shopping_cart

shopping_cart_function()


# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# In[19]:


import modforhw
modforhw.mod_1(4,6)


# In[21]:


import modforhw
modforhw.mod_2(5)


# In[ ]:




