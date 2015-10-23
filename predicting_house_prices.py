import fileinput
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression

#######Extract the Training and Testing data
i=-1
for line in fileinput.input():
    if i==-1:
        no_feature=int(line.split(" ")[0])
        no_row=int((line.split(" ")[1]))
        training_feature=[]
        training_class=[]
        testing_feature=[]
        i=0
    elif i<no_row:
        training_vector= [float(x) for x in line.split(" ")]
        training_feature.append(training_vector[0:-1])
        training_class.append(training_vector[-1])
        i=i+1
    else:
        testing_vector=[float(x) for x in line.split(" ")]
        if len(testing_vector)>1:
            testing_feature.append(testing_vector)
            
#######Build the Model
model =LinearRegression().fit(training_feature, training_class)

#######Predict the Output
prediction =model.predict(testing_feature)
for each_prediction in prediction:
    print each_prediction
