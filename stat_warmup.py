import numpy as np
import math
import scipy as sp
from scipy import stats
import math
import fileinput


#####Calculate the Threshold Boundary of the 95% Confidence Interval for the mean 
def mean_confidence_interval(data, confidence=0.95):
    num_data = len(data)
    std = np.std(data)
    boundary_threshold = 1.96*std/(math.sqrt(num_data))
    return boundary_threshold

######Extract the data
i=-1
for line in fileinput.input():
    if i==-1:
        count=0
        i=i+1
    if i==0:
        data=[int(x) for x in line.split(" ")]

######Convert data to numpy array        
data_list = np.array(data)

######Find the frequency of each value in the data
counts = np.bincount(data_list)

######Find 95% Confidence Interval for the mean
boundary_threshold=mean_confidence_interval(data)

######Find the Lower and Upper Boundary of the 95% Confidence Interval for the mean
lower_boundary=np.mean(data)-boundary_threshold
upper_boundary=np.mean(data)+boundary_threshold

print np.mean(data) ####  Mean of the data
print np.median(data) ####  Median of the data
print np.argmax(counts) ####  Mode of the data
print np.std(data) #### Standard deviation of the data
print lower_boundary, upper_boundary




