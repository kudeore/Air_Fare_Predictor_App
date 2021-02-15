# Flight Fare Prediction: 

An app usefull to predict the prices of airlines based on date and time of journey , as well as type of airlines and number of stops . 
Predictions are based on the historical data used to train the model. 

## Content
  * [Visuals](#Visuals)
  * [Overview](#Overview)
  * [Cloud Deployment Heroku ](#Cloud_Deployment_Heroku)
  * [Directory Tree](#directory-tree)
  * [Am I missing Something?](#Am I missing Something?)


## Demo
Link:https://airfarepred.herokuapp.com/

[![](https://i.imgur.com/tDGWSWC.png)](https://heroku.com)


## Overview
Predict the prices of airlines based on date and time of journey , as well as type of airlines and number of stops .


## Installation
Install all dependancies using following command after cloning [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
- Signup on heroku.come 
- To deploy on heroku we need heroku ctl to be downloaded 

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

- Next step is to create heroku app with name as per availability 
- We need to push the code on heroku using Git commit 
- detail steps are given in the documentation (for documentation visit Heroku website) 
- [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python)

Importatnt Things to make note of while deploying model to Heroku free cloud . 
- Heroku provides max 500MB sludge memory 
- If we have big model , its not possible to deploy it on Heroku Cloud. 


## Directory Tree 
```
├── static 
│   ├── css
│      ├── style.css
├── images 
│   ├── flight.jpeg
├── templates
│   ├── home.html
├── Preprocessing.py
├── feature_selection.py
├── app.py
├── Procfile
├── README.md
├── model.pkl
├── requirements.txt
```

- model.pkl is not copied to repo , as size is to huge 
- Please run Preprocessing.py in your local machine first to get model.pkl 

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/Vgxcuk1.png" width=170>]
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


## Am I missing Something?

- **Nothing is impossible!**
- please open an [issue](https://github.com/kudeore/Flight_price_pred_AWS_APP/issues) and lets make it better together 
- *Bug reports, feature requests, patches, and well-wishes are always welcome.* :heavy_exclamation_mark:



