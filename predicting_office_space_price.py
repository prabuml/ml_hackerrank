import fileinput
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#######Extract the Training and Testing data

i=-1
for line in fileinput.input():
    if i==-1:
        no_feature= int(line.split(" ")[0])
        no_row = int(line.split(" ")[1])
        
        training_feature= []
        training_class=[]
        testing_feature=[]
        i=0
    elif i<no_row:
        training_vector= [float(x) for x in line.split(" ")]
        training_feature.append(training_vector[0:-1])
        training_class.append(training_vector[-1])
        i=i+1
    else:
        testing_vector= [float(x) for x in line.split(" ")]
        if len(testing_vector)>1:
            testing_feature.append(testing_vector)

#######Transform the features
poly = PolynomialFeatures(degree=2)
processed_training_feature = poly.fit_transform(training_feature)

#######Build the Model
model = LinearRegression().fit(processed_training_feature,training_class)
testing_processed = poly.fit_transform(testing_feature)

#######Predict the Output
prediction=model.predict(testing_processed)
for each_prediction in prediction:
    print each_prediction
