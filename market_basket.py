# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:08:51 2020

@author: Shuvo
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('Market_Basket_Optimisation.csv')
store_data = pd.read_csv('Market_Basket_Optimisation.csv', header=None) 
num_records=len(store_data)
records=[]
for i in range(0,num_records):
    records.append([str(store_data.values[i,j]) for j in range(0,20) ])
    
    
association_rules = apriori(records, min_support=0.0045, min_confidence=0.3, min_lift=3, min_length=3)
association_results = list(association_rules)
results=[]
for item in association_results:
    pair=item[0]
    items=[x for x in pair]
    value0=str(items[0])
    value1=str(items[1])
    value2=str(item[1:7])
    value3=str(item[2][0][2])[:7]
    value4=str(item[2][0][3])[:7]
    rows=(value0,value1,value2,value3,value4)
    results.append(rows)
    label=['title1','title2','support','confidence','lift']
    store_suggestion=pd.DataFrame.from_records(results,columns=label)
    print( store_suggestion)
