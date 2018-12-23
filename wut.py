'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import time
from datetime import datetime
plt.rcParams['figure.figsize'] = [16,10]

data = pd.read_csv("records.csv")

train,test = train_test_split(data,test_size=0.25)

train_target = train.plan

train = train.drop(columns="plan")

train_id = train.pop("id")

feature = ["age","salary","gender","relationship_status","education","employment_status"]

train_v1 = train[feature]

train_train,train_train_target,train_valid,train_valid_target = train_test_split(train_v1,train_target,test_size=0.2,random_state=13)

test_target = test.pop("plan")

categorical_variables = ["gender","relationship_status","education","employment_status"]

for variable in categorical_variables:
    dummies = pd.get_dummies(train_v1[variable],prefix=variable,prefix_sep='_')
    train_v1 = pd.concat([train_v1, dummies],axis=1)
    #train_v1.drop([variable,axis=1,inplace=True])

train_v1 = train_v1.drop(columns=categorical_variables)

test_v1 = test[feature]

categorical_variables = ["gender","relationship_status","education","employment_status"]

for variable in categorical_variables:
    dummies = pd.get_dummies(test_v1[variable],prefix=variable,prefix_sep='_')
    test_v1 = pd.concat([test_v1, dummies],axis=1)
    #test.drop([variable,axis=1,inplace=True])
test_v1 = test_v1.drop(columns=categorical_variables)

train_train,train_valid,train_train_target,train_valid_target = train_test_split(train_v1,train_target,test_size=0.2,random_state=13)

train_train.salary = train_train.salary/100
train_valid.salary = train_valid.salary/100

dtrain = xgb.DMatrix(train_train, label = train_train_target)
dvalid = xgb.DMatrix(train_valid, label = train_valid_target)
dtest = xgb.DMatrix(test_v1)
watchlist = [(dtrain,'train'),(dvalid,'valid')]

'''

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb

model = pickle.load(open("model.dat","rb"))
#Here the test array will have variables from the data mined through social media sites like Facebook, Twitter, Glassdoor
#test = [age,salary,gender,relationship_status,education,employment_status] #one hot coding
#test = [51,331751,male,married,g,unemployed]
test = [51,331751,0,1,1,0,0,0,1,0,0,0,1]

pred = model.predict(test)
print pred
