import math

####Calculate mean of the data
def mean(data):
    return float(sum(data))/len(data)

####Calculate std of the data
def std(data,mean):
    sum_data=0
    for x in data:
        sum_data=sum_data+math.pow(x-mean,2)
    sum_data=float(sum_data)/(len(data)-1)
    sum_data=math.sqrt(sum_data)
    return sum_data

#####Calculate the correction between vectors
def correlation(a,a_mean,a_std,b,b_mean,b_std):
    n=len(a)
    sum_data=0
    for i in range(0,n):
        sum_data=sum_data+a[i]*b[i]
    sum_data = sum_data - a_mean*b_mean*n    
    div = (n-1)*a_std*b_std
    correlated_value = float(sum_data)/div
    return correlated_value
   
####Extract the math, phys, chem features    
import fileinput
i=-1
maths=[]
phys=[]
chem=[]
for line in fileinput.input():
    if i==-1:
        no_feature= int(line.split(" ")[0])
        i=i+1
    else:
        d=line.split("\t")
        maths.append(int(d[0]))
        phys.append(int(d[1]))
        chem.append(int(d[2]))
    
    
####Extract the math, phys, chem mean
math_mean=mean(maths)
phys_mean=mean(phys)
chem_mean=mean(chem)

####Extract the math, phys, chem std
math_std=std(maths,math_mean)
phys_std=std(phys,phys_mean)
chem_std=std(chem,chem_mean)

#### Print Correlation between features
print round(correlation(maths,math_mean,math_std,phys,phys_mean,phys_std),2)
print round(correlation(chem,chem_mean,chem_std,phys,phys_mean,phys_std),2)
print round(correlation(maths,math_mean,math_std,chem,chem_mean,chem_std),2)
