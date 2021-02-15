#!/usr/bin/env python
# coding: utf-8

# In[7]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import feature_selection
from Preprocessing import preprocessing_datetime, preposses_encoding


# In[3]:


final_features = feature_selection.selected_features


# In[5]:


df = pd.read_excel(r"data\Data_Train.xlsx")


# In[8]:


df = preprocessing_datetime(df)
df= preposses_encoding(df)


# In[13]:


X = df[final_features]
X= X.fillna(0)


# In[14]:


Y= df["Price"]


# In[15]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)


# In[16]:


from sklearn.ensemble import RandomForestRegressor
reg_rf = RandomForestRegressor()
reg_rf.fit(X_train, y_train)


# In[17]:


y_pred = reg_rf.predict(X_test)


# In[18]:


reg_rf.score(X_train, y_train)


# In[19]:


reg_rf.score(X_test, y_test)


# In[25]:


plt.figure(figsize=(12,10))
sns.scatterplot(x= y_test, y=y_pred)


# In[26]:


from sklearn import metrics


# In[27]:


metrics.r2_score(y_test, y_pred)


# In[28]:


#Hyperparameter optimisation 


# In[29]:


from sklearn.model_selection import RandomizedSearchCV


# In[31]:


# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)


# In[33]:


# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(X_train, y_train)


# In[34]:


rf_random.best_params_


# In[35]:


prediction = rf_random.predict(X_test)


# In[36]:


plt.figure(figsize=(12,10))
sns.scatterplot(x= y_test, y=y_pred)


# In[37]:


print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))


# In[38]:


#dumping model parametrs for next use 


# In[39]:


import pickle


# In[41]:


pickle.dump(rf_random, open('model.pkl','wb'))


# In[42]:


model = open('model.pkl','rb')


# In[44]:


rf = pickle.load(model)


# In[45]:


pred= rf.predict(X_test)


# In[46]:


print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred)))


# In[48]:





# In[50]:





# In[ ]:




