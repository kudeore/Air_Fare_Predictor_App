#!/usr/bin/env python
# coding: utf-8

# In[51]:


from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


# In[52]:


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


# In[53]:


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


# In[54]:


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
         # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_date = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journy_Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)
        
        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        dep_time = Dep_hour + Dep_min/60
        # print("Departure : ",Dep_hour, Dep_min)
        
        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        arrival_time = Arrival_hour + Arrival_min/60
        # print("Arrival : ", Arrival_hour, Arrival_min)
        
        #duration 
        dur = arrival_time - dep_time
        
        # Total Stops
        Total_Stops = float(request.form["stops"])
        # print(Total_stops)
        
        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Airline_Jet_Airways = 1
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='IndiGo'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 1
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Air India'):
            Airline_Jet_Airways= 0
            Airline_IndiGo = 0
            Airline_Air_India = 1
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Multiple carriers'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 1
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0  
            
        elif (airline=='SpiceJet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 1
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0  
            
        elif (airline=='Vistara'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 1
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='GoAir'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 1
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Multiple carriers Premium economy'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 1
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        elif (airline=='Jet Airways Business'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 1
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 

        elif (airline=='Vistara Premium economy'):
            Airline_Jet_Airwayss = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 1
            Airline_Trujet = 0 
            
        elif (airline=='Trujet'):
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 1 
            
        else:
            Airline_Jet_Airways = 0
            Airline_IndiGo = 0
            Airline_Air_India = 0
            Airline_Multiple_carriers = 0
            Airline_SpiceJet = 0
            Airline_Vistara = 0
            Airline_GoAir = 0
            Airline_Multiple_carriers_Premium_economy = 0
            Airline_Jet_Airways_Business = 0
            Airline_Vistara_Premium_economy = 0
            Airline_Trujet = 0 
            
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            Source_Delhi = 1
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Kolkata'):
            Source_Delhi = 0
            Source_Kolkata = 1
            Source_Mumbai = 0
            Source_Chennai = 0

        elif (Source == 'Mumbai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 1
            Source_Chennai = 0

        elif (Source == 'Chennai'):
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 1

        else:
            Source_Delhi = 0
            Source_Kolkata = 0
            Source_Mumbai = 0
            Source_Chennai = 0
            
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
        
        elif (Destination == 'Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'New_Delhi'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif (Destination == 'Kolkata'):
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            
        prediction=model.predict([[               
            Total_Stops,
            journy_Month,
            journey_date,
            arrival_time,
            dep_time,
            dur,
            Airline_Air_India,
            
            Airline_IndiGo,
            Airline_Jet_Airways,
            Airline_Jet_Airways_Business,
            Airline_Multiple_carriers,
            Airline_Multiple_carriers_Premium_economy,
            Airline_SpiceJet,
            
            Airline_Vistara,
            
            
            Source_Delhi,
           
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
           
            Destination_New_Delhi
        ]])
        
        output=round(prediction[0],2)
        
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
    
    return render_template("home.html")



# In[55]:


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


# In[ ]:




