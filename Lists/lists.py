# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

#creating a list
mylist = []
mylist = [1,5,"hello"]
mylist = [1,"hello",[3,5,7]]

# added 7 in mylist
mylist.append(7)

#deleted hello in mylist
mylist.remove("hello")

# lenght of mylist 
print(len(mylist))

# how many has 7 in mylist 
mylist.count(7)

# sorting the elements
mylist.sort()

#reversing the order of the elements
mylist.reverse()

#clearing mylist 
mylist.clear()