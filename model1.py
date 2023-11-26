import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import pickle
data=pd.read_excel('/workspaces/Python_Flask/dataset/iris .xls')
le = LabelEncoder()
data['Classification']= le.fit_transform(data['Classification'])
y = data['Classification']
x = data.drop(['Classification'],axis=1)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = .25,random_state=42)
from sklearn.ensemble import RandomForestClassifier
rf_cls = RandomForestClassifier(n_estimators= 12)
model_rf = rf_cls.fit(x_train,y_train)
y_pred_rf = model_rf.predict(x_test)
pickle.dump(model_rf,open('model.pkl','wb'))