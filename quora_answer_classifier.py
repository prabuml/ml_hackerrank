import fileinput
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import  GaussianNB
from sklearn import preprocessing

import pandas as pd
import numpy as np

#######Extract the Training data and Testing data
i=-1
training_data=[]
testing_data = []
min_temp =[]
max_temp = []
for line in fileinput.input():
    if i==-1:
        n=int(line.split(" ")[0])
        m=int(line.split(" ")[1])
        i=i+1
    elif i<n:
        training_data.append(line.replace("\n",""))
        i=i+1
    elif i==n:
        test_size = line
        i=i+1
    else:
        testing_data.append(line.replace("\n",""))
        
###### Extract training_feature and training_class
training_feature= []
training_class = []

for x in training_data:
    y =x.split(" ")
    training_class.append(int(y[1]))
    training_feature.append([float(y1.split(":")[1]) for y1 in y[2:]])
    
    
###### Extract testing_feature and testing_class

testing_feature = [] 
testing_id = []
for x in testing_data:
    y =x.split(" ")
    testing_feature.append([float(y1.split(":")[1]) for y1 in y[1:]])
    testing_id.append(y[0])

    
####### Build the Model  
clf =RandomForestClassifier(n_estimators=20).fit(training_feature, training_class)

#######Predict the Output
prediction = clf.predict(testing_feature)
for i in range(len(prediction)):
    if prediction[i]==1:
        print testing_id[i]+" +1"
    else:
        print testing_id[i]+" -1"

