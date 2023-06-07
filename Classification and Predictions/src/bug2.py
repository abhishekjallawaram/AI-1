# -*- coding: utf-8 -*-
"""Bug2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-9txPn77R9dNWOCJy57zPCAyijIh8VbQ
"""

import re
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB,GaussianNB
from imblearn.over_sampling import SMOTE
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,f1_score,make_scorer
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.impute import SimpleImputer
from sklearn.model_selection import ShuffleSplit,cross_val_score

bug2 = pd.read_csv("/content/drive/MyDrive/data_bug2.txt", sep=' ')
bug2.info()
print(bug2.shape)
bug2.head(7)

bug2.describe()

d_label = bug2['d']

bug2.drop(['d'],axis=1,inplace = True)

X_train, X_test, y_train, y_test = train_test_split(bug2, d_label, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train1 = scaler.fit_transform(X_train)
print(scaler.mean_)
X_test1 = scaler.transform(X_test)

print(type(X_train1))
print(type(X_test1))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR


classifiers_list = {
    "K-Neighbors Regressor": KNeighborsRegressor(),
    "Decision Tree Regressor": DecisionTreeRegressor(),
    "Random Forest Regressor": RandomForestRegressor(),
    "Naive Bayes Regressor" : GaussianProcessRegressor(),
    "Neural Network Regressor" : MLPRegressor(),
    "Adaboost" : AdaBoostRegressor(base_estimator=RandomForestRegressor()),
    "SVR": SVR()                           
}

classifiers_count = len(classifiers_list.keys())
df_results = pd.DataFrame(data=np.zeros(shape=(classifiers_count,5)), columns = ['classifier', 'Recall', 'F1', 'Precision', 'Accuracy'])

for c_name, classifier in classifiers_list.items():
  classifier.fit(X_train,y_train)
  prediction = []
  prediction = classifier.predict(X_test)
  cv1 = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
  scores = cross_val_score(classifier, X_train, y_train, cv=cv1)
  print ('Classifier+OneHotEncoder', c_name)
  print ('Cross validation', scores)
  print(prediction)
  #print(classification_report(y_test,prediction))
  print(mean_squared_error(y_test,prediction, squared=False))

classifiers_list = {
    "K-Neighbors Regressor": KNeighborsRegressor(),
    "Decision Tree Regressor": DecisionTreeRegressor(),
    "Random Forest Regressor": RandomForestRegressor(),
    #"Naive Bayes Regressor" : GaussianProcessRegressor(),
    "Neural Network Regressor" : MLPRegressor()
}

classifiers_count = len(classifiers_list.keys())
df_results = pd.DataFrame(data=np.zeros(shape=(classifiers_count,5)), columns = ['classifier', 'Recall', 'F1', 'Precision', 'Accuracy'])

for c_name, classifier in classifiers_list.items():
  classifier.fit(X_train1,y_train)
  prediction = []
  prediction = classifier.predict(X_test1)
  cv1 = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
  scores = cross_val_score(classifier, X_train1, y_train, cv=cv1)
  print ('Classifier+OneHotEncoder', c_name)
  print ('Cross validation', scores)
  print(prediction)
  #print(classification_report(y_test,prediction))
  print(mean_squared_error(y_test,prediction, squared=False))

print(y_test)

import sklearn.metrics
print(sklearn.metrics.SCORERS.keys())

from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# Define our candidate hyperparameters
hp_candidates = [{'n_neighbors': [2,3,4,5,6,7,8,9,10,11,12,13,14,15], 'weights': ['uniform','distance'],'p':[1,2,5]}]

# Search for best hyperparameters
grid = GridSearchCV(estimator=KNeighborsRegressor(), param_grid=hp_candidates, cv=5,scoring='r2')

grid.fit(X_train1,y_train)

print("Tuned Hyperparameters :", grid.best_params_)
print("Accuracy :",grid.best_score_)

hp_candidates = [{"max_depth" : [None,2,4,6,8,10,12], }]
grid = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid=hp_candidates, cv=5)
grid.fit(X_train1,y_train)

print("Tuned Hyperparameters :", grid.best_params_)
print("Accuracy :",grid.best_score_)

hp_candidates = [{'n_estimators': [10,20,30,40],'max_features': ['auto', 'sqrt', 'log2'],'max_depth' : [None,2,3,4,5]}]
grid = GridSearchCV(estimator=RandomForestRegressor(), param_grid=hp_candidates, cv=5,scoring='neg_mean_absolute_error')
grid.fit(X_train1,y_train)

print("Tuned Hyperparameters :", grid.best_params_)
print("Accuracy :",grid.best_score_)

classifiers_list = {
    "K-Neighbors Regressor": KNeighborsRegressor(n_neighbors = 2, p = 2, weights = 'distance'),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth= None),
    "Random Forest Regressor": RandomForestRegressor(max_depth= None, max_features = 'auto', n_estimators = 40),
    #"Naive Bayes Regressor" : GaussianProcessRegressor(),
    "Neural Network Regressor" : MLPRegressor()
}

classifiers_count = len(classifiers_list.keys())
df_results = pd.DataFrame(data=np.zeros(shape=(classifiers_count,5)), columns = ['classifier', 'Recall', 'F1', 'Precision', 'Accuracy'])

for c_name, classifier in classifiers_list.items():
  classifier.fit(X_train1,y_train)
  prediction = []
  prediction = classifier.predict(X_test1)
  cv1 = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
  scores = cross_val_score(classifier, X_train1, y_train, cv=cv1)
  print ('Classifier+OneHotEncoder', c_name)
  print ('Cross validation', scores)
  print(prediction)
  #print(classification_report(y_test,prediction))
  print(mean_squared_error(y_test,prediction, squared=False))

# Commented out IPython magic to ensure Python compatibility.
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt
# %matplotlib inline
rmse_val = [] #to store rmse values for different k
for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)

    model.fit(X_train, y_train)  #fit the model
    pred=model.predict(X_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val) #elbow curve 
curve.plot()

hp_candidates = [{"max_depth" : [1,3,5,7,9,None],"min_samples_leaf":[2,3,4,5],"max_leaf_nodes":[None,10,20]}]
grid = GridSearchCV(estimator=DecisionTreeRegressor(), param_grid=hp_candidates, cv=5)
grid.fit(X_train1,y_train)

print("Tuned Hyperparameters :", grid.best_params_)
print("Accuracy :",grid.best_score_)

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# Define our candidate hyperparameters
hp_candidates = [{'n_neighbors': [2,3,4,5,6,7,8,9,10,11,12,13,14,15], 'weights': ['uniform','distance'],'p':[1,2,5]}]

# Search for best hyperparameters
grid = GridSearchCV(estimator=KNeighborsRegressor(), param_grid=hp_candidates, cv=5)

grid.fit(X_train1,y_train)

print("Tuned Hyperparameters :", grid.best_params_)
print("Accuracy :",grid.best_score_)

rmse_val = [] #to store rmse values for different k
for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors=K,p=2,weights='distance')

    model.fit(X_train, y_train)  #fit the model
    pred=model.predict(X_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)

curve = pd.DataFrame(rmse_val) #elbow curve 
curve.plot()

from sklearn import tree
text_representation = tree.export_text(regr)
print(text_representation)

fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(regr, feature_names=['x','y','dx','dy'], filled=True)