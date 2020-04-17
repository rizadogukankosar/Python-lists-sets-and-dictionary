# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

#creating a set

myset = {0,1,2}

#printing the elements
for number in myset:
    print(number)

# adding an element
myset.add(3)

# adding elements 
myset.update([4,5,6])

# deleting 0 in myset
myset.remove(0)

#deleting 0 in myset but if myset has't 0, you don't take exception 
myset.discard(0)

myset2 = {6,7,8}

# myset and myset2 unit but 6 not write two times
print(myset.union(myset2)) #{1,2,3,4,5,6,7,8}
            #or
print(myset | myset2) #{1,2,3,4,5,6,7,8}

#printing common element of myset and myset2
print(myset & myset2)  # 6 
            #or
print(myset.intersection(myset2)) # 6 

