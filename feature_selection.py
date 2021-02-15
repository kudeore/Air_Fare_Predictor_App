#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

import Preprocessing


# In[37]:


df = pd.read_excel(r"data\Data_Train.xlsx")


# In[38]:


pd.set_option('display.max_columns', None)


# In[39]:


df = Preprocessing.preprocessing_datetime(df)


# In[40]:


df = Preprocessing.preposses_encoding(df)


# In[41]:


df.head()


# In[42]:


#selct the best feature by using sklearn Extra tree regressor 
#first separate dependent and independen features 


# In[43]:


X = df.drop(["Price"], axis = 1)


# In[49]:


X = X.fillna(0)


# In[46]:


Y = df["Price"]


# In[70]:


from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler


# In[71]:


Sc = StandardScaler()


# In[72]:


X= Sc.fit_transform(X)


# In[91]:


lasso = LassoCV().fit(X, Y)
importance = np.abs(lasso.coef_)


# In[92]:


#importance = np.sort(importance)
#importance


# In[115]:


from sklearn.feature_selection import SelectFromModel
from time import time

threshold = np.sort(importance)[-20] + 0.01

tic = time()
sfm = SelectFromModel(lasso, threshold=threshold).fit(X, Y)
toc = time()
print(threshold)


# In[116]:


features = df.drop(["Price"],axis=1).columns


# In[117]:


plt.figure(figsize= (16,10))
sns.barplot(x=importance, y=features)


# In[118]:


selected_features= features[sfm.get_support()]


# In[121]:


print(len(selected_features), len(features))


# In[126]:


selected_features


# In[130]:


features


# In[141]:


df1 = df[selected_features]


# In[ ]:





# In[ ]:




