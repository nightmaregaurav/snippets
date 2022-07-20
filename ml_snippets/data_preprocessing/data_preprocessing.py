"""
@author: NightmareGaurav
"""

import numpy as py
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv('DataSet.csv')
X=dataset.iloc[:,:-1].values
XX=dataset.iloc[:,:-1].values
XXX=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

# MEAN strategy
imputer=SimpleImputer(missing_values = py.nan , strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print("Prediction By Mean: ")
print(X[:, 1:3])

# Median
imputer=SimpleImputer(missing_values = py.nan , strategy = 'median')
imputer = imputer.fit(XX[:, 1:3])
XX[:, 1:3] = imputer.transform(XX[:, 1:3])

print("Prediction By Median: ")
print(XX[:, 1:3])

# most frequent data
imputer=SimpleImputer(missing_values = py.nan , strategy = 'most_frequent')
imputer = imputer.fit(XXX[:, 1:3])
XXX[:, 1:3] = imputer.transform(XXX[:, 1:3])

print("Prediction By Most frequent: ")
print(XXX[:, 1:3])

onehotencoder=OneHotEncoder()
X=onehotencoder.fit_transform(X).toarray()

#Training and Testing Data (divide the data into two part)
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.2, random_state=0)

#Standard and fit the data for better predication
sc_X=StandardScaler()
X_test=sc_X.fit_transform(X_test)
X_train=sc_X.fit_transform(X_train)
