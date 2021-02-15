#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


def preprocessing_datetime(data): 
    data.fillna(0)
     ## covert data data to day and month 
    data['journy_Month'] = pd.DatetimeIndex(data['Date_of_Journey']).month
    data['journey_date'] = pd.DatetimeIndex(data['Date_of_Journey']).day
    # droping original journey date column
    data.drop(["Date_of_Journey"], axis = 1, inplace = True)
    
    #extract time from arrival time date , in terms of int 
    data["Arrival_hour"] = pd.to_datetime(data.Arrival_Time).dt.hour
    data["Arrival_min"] = pd.to_datetime(data.Arrival_Time).dt.minute
    
    data["arrival_time"] = data["Arrival_hour"] + data["Arrival_min"]/60
    #drop original column 
    data.drop(["Arrival_Time"], axis = 1, inplace = True)
    data.drop(["Arrival_hour"], axis = 1, inplace = True)
    data.drop(["Arrival_min"], axis = 1, inplace = True)
    
    #extract dep time from dep time 
    
    data["Dep_hour"] = pd.to_datetime(data["Dep_Time"]).dt.hour
    data["Dep_min"] = pd.to_datetime(data["Dep_Time"]).dt.minute
    data["dep_time"] = data["Dep_hour"] + data["Dep_min"]/60
    
    #  drop Dep_Time as it is of no use
    data.drop(["Dep_Time"], axis = 1, inplace = True)
    data.drop(["Dep_hour"], axis = 1, inplace = True)
    data.drop(["Dep_min"], axis = 1, inplace = True)
    
    # conver data for duration to required formate 
    #separate 2h 50m formate first by space 
    data[["H","M"]] =data["Duration"].str.split(" ", n = 1, expand = True) 
    
    #for each column of houre and minute , separate text and column 
    data['H'] = data['H'].str.extract('(\d+)').astype(float)
    data["H"] = data["H"].fillna(0)
    data["H"] = data["H"].astype(int)
    
    #same for minutes 
    
    data['M'] = data["M"].str.extract('(\d+)').astype(float)
    data["M"] = data["M"].fillna(0)
    data["M"] = data["M"].astype(int)
    
    #merge these columns to get duration 
    
    data["dur"] = data["H"] + data["M"]/60
    
    #drop unnecessary columns 
    data.drop(["Duration"], axis = 1, inplace = True)
    #data.drop(["h"], axis = 1, inplace = True)
    data.drop(["M"], axis = 1, inplace = True)
    data.drop(["H"], axis = 1, inplace = True)
    
    #drop rout data and add info 
    
    data.drop(["Route", "Additional_Info"], axis=1, inplace = True)
    
    return data

def preposses_encoding(data): 
    
    #covert nominal data for Airline , source and destination using one hot encoder 
    Airline = data[["Airline"]]
    Airline = pd.get_dummies(Airline, drop_first= True)
    
    Source = data[["Source"]]
    Source = pd.get_dummies(Source, drop_first= True)
    
    Destination = data[["Destination"]]
    Destination = pd.get_dummies(Destination, drop_first= True)
    
       
    #concate one hot encoded columns
    
    data = pd.concat([data, Airline, Source, Destination], axis = 1)
    
    # lable encoding for number of stops
    
    data.replace({"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}, inplace = True)
    
    data.drop(["Airline", "Source", "Destination"], axis = 1, inplace = True)
    
    return data
    


# In[ ]:





# In[ ]:




