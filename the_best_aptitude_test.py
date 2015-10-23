
import fileinput
import numpy as np
from scipy.signal import correlate
from scipy.stats.stats import pearsonr 

##### Extract the data
i=-1
gpa=[]
score=[]
for line in fileinput.input():
    if i<0:
        temp=line
    elif i==1:
        gpa=[float(x) for x in line.split(" ")]
    elif i%7==0:
        temp=line
    elif i%7-1==0 and i!=1:
        count=0
        max_correlation=-10
        index=-1
        for x in score:
            count=count+1    
            if pearsonr(x,gpa)[0] >= max_correlation:
                max_correlation = pearsonr(x,gpa)[0]
                index=count
        print index        
        gpa=[float(x) for x in line.split(" ")]
        score=[]
    else:
        score_each = [float(x) for x in line.split(" ")]
        score.append(score_each)
    i=i+1

##### Pick the Grade which has the maximum correlation
count=0
max_correlation=-10
index=-1
for x in score:
    count=count+1    
    if pearsonr(x,gpa)[0] >= max_correlation:
        max_correlation = pearsonr(x,gpa)[0]
        index=count
print index

        
        
     
