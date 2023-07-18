# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:38:07 2023

@author: User
"""

class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self): 
        print("Name:"+self.citizen_name)
        print("age:"+str(self.citizen_age))
        print("Date of birth:"+self.citizen_dob)
        print("citizen Id:"+self.citizen_id)
        print(" official canadian citizen ")
    
    
citizen1 = Citizen("aleena",13,"3rd october 2010","0198")
citizen1.add_citizen()
citizen2 = Citizen("arshi",23,"18th april 2000","0199")
citizen2.add_citizen()
citizen3 = Citizen("sahil",24,"6th july 1999","0200")
citizen3.add_citizen()
citizen4 = Citizen("didar",54,"16th september 1969","0201")
citizen4.add_citizen()
citizen5 = Citizen("sonia",48,"22nd november 1975","0202")
citizen5.add_citizen()
        