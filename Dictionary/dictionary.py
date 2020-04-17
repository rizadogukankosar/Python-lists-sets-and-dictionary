# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:45:52 2020

@author: doguk
"""  

#Dictionary        
             #Key -> Value
translator = {
    "computer" : "bilgisayar",
    "screen" : "ekran"
    }

print(translator["computer"])  #printed bilgisayar

#adding new values
translator["keyboard"] = "klavye"

#deleting a value with key
del(translator["screen"])

#printing lenght of translator
print(len(translator))



