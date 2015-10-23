import numpy as np
from scipy import interpolate
import fileinput

#####Extract the price value
i=-1
prices = []
for line in fileinput.input():
    if i==-1:
        n=int(line)
        i=i+1
    else:
        prices.append(line.split("\t")[1])

        
#####Extract the training and testing data
training_feature = []
training_output = []
testing_feature = []
for i in xrange(n):
    if not "Missing" in prices[i]:
        training_feature.append(i)
        training_output.append(float(prices[i]))
    else:
        testing_feature.append(i)
y = np.array(training_feature)

#####Build the Model
model = interpolate.UnivariateSpline(training_feature, training_output, s=1)

#####Predict the Output
for each_feature in testing_feature:
    print model(each_feature)
