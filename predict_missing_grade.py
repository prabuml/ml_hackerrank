import fileinput
import json
from sklearn.linear_model import SGDRegressor
import itertools


#######Extract the Testing data
i=-1
testing_data=[]
for line in fileinput.input():
    if i==-1:
        no_test=int(line.split(" ")[0])
        i=i+1
    else:
        testing_data.append(json.loads(line))        

#######Extract the Training data
training_data = []
with open('training.json') as f:
    for line in f:
        training_data.append(json.loads(line))

#######Extract the unique features
unique_keys = [x.keys() for x in training_data[1:]]
unique_keys = list(set(list(itertools.chain(*unique_keys))))
unique_keys.remove('Mathematics')
unique_keys.remove("serial")

####### Assign a class (number) to each grade
count=-1
training_set = {}
training_inverse_set = {}
for x in unique_keys:
    count=count+1
    training_set[x]=count
    training_inverse_set[count] = x
    
#### Extract the training features    
training_features = []
training_serial = []
training_class = []
for x in training_data[1:]:
    each_training = [0,0,0,0,0,0,0,0,0]
    for each_data in x:
        if 'Mathematics' == each_data:
            training_class.append(x[each_data])
        elif 'serial' == each_data:
            training_serial = x[each_data]
        else:
            each_training[training_set[each_data]] = x[each_data]
    training_features.append(each_training)

#### Extract the testing features
testing_features = []
testing_serial = []
testing_class = []
for x in testing_data:
    each_testing = [0,0,0,0,0,0,0,0,0]
    for each_data in x:
        if 'Mathematics' == each_data:
            testing_class.append(x[each_data])
        elif 'serial' == each_data:
            testing_serial = x[each_data]
        else:
            each_testing[training_set[each_data]] = x[each_data]
    testing_features.append(each_testing)

##### Build the model
model = SGDRegressor(penalty='l2',loss='epsilon_insensitive').fit(training_features, training_class)

##### Predict the test data
prediction = model.predict(testing_features)
for each_prediction in prediction:
    print int(each_prediction)

