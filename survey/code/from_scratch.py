#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:38:04 2019

@author: andre
"""

import pandas as pd
import csv
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"""
keys:

    a03--Gender
    a06--City
    a05--State
    a04--Country
    b02--Formation
    b01--Highest degree
    b03--affilliated
    b04--which one
    
    
"""





def load_tsv(filename):
    data = pd.read_csv(filename, delimiter="\t")
    return data

def get_header_position(data,header_string="Country"):
    position = data.filter(like=header_string)
    
    return position

def organize_by_header(data,header_string="Country"):
    header = data.filter(like=header_string)
    dummie = pd.DataFrame(index=header.values,data=data.values, columns = data.columns) 
    return dummie

filename = "test"
data = load_tsv(filename=filename)
byCountry = organize_by_header(data,header_string="Country")


# plot example with respondents from france
france = byCountry.filter(like="France",axis=0)
frGender = get_header_position(france,"Gender")
#frGender.

plt.plot(france)     


#new_equipment1["keys"]=list(new_equipment1.keys())
#new_equipment2["keys"]=list(new_equipment2.keys())

df1 = pd.DataFrame.from_dict(new_equipment1,orient="index")
df2 = pd.DataFrame.from_dict(new_equipment2,orient="index")
df3 = pd.DataFrame.from_dict(new_equipment3,orient="index")

df1.index.name = "equipment"
df2.index.name = "equipment"
df3.index.name = "equipment"
#df1 = df1.transpose()
#df1 = df1.set_index("keys")
#df1 = df1.transpose()

#df2 = df2.transpose()
#df2 = df2.set_index("keys")
#df2 = df2.transpose()

test = df1.join(df2, on="equipment",lsuffix="1",rsuffix="2")
test = test.join(df3, on="equipment",lsuffix="3",rsuffix="4")

# make the columns be increasing numbers from 0 to max num
test.columns = list(range(len(test.columns)))

# substitute nans and nones for zeros
test = test.fillna(0)
#save it as csv
test.to_csv("test.csv")

print("results are:\n")

equipment=list()
quantity=list()
for key in test.index:
    
    tempsum = np.sum(test.loc[key]!=0)
    equipment.append(key)
    quantity.append(tempsum)
    #print(key +": "+str(tempsum))

ordered = sorted(zip(quantity,equipment),reverse=True)
dummie1 = [x for _,x in sorted(zip(quantity,equipment))]
dummie2 = [x for x,_ in sorted(zip(quantity,equipment))]
equipment = pd.DataFrame.from_dict(equipment,orient="index")
equipment.columns.name = "quantity"

print(ordered)