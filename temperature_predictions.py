import fileinput
import pandas as pd
import numpy as np

#####Extract the minimum and maximum temperature data
#####   Append NA (empty value) to missing value
#####   Store the location of missing value in missing_dict
i=-2
temperature=[]
min_temp =[]
max_temp = []
missing_dict={}
for line in fileinput.input():
    if i==-2:
        no_test=int(line.split(" ")[0])
        i=i+1
    elif i==-1:
        i=i+1
    else:
        temperature_list = line.split("\t")
        if "Missing" not in temperature_list[2]:
            min_temp.append(float(temperature_list[2]))
        else:
            missing_dict[int(temperature_list[2].replace("Missing_","").replace("\n",""))]=['min',i]
            min_temp.append(np.nan)
        if "Missing" not in temperature_list[3]:
            max_temp.append(float(temperature_list[3].replace("\n","")))
        else:
            max_temp.append(np.nan)
            missing_dict[int(temperature_list[3].replace("Missing_","").replace("\n",""))]=['max',i]
        i=i+1
        
##### Interpolate the data i.e fill the missing value     
d = {'min' : pd.Series(min_temp),'max' : pd.Series(max_temp)}
df = pd.DataFrame(d)
df_processed = df.interpolate()

##### Print the filling missing value
for x in sorted(missing_dict.keys()):
    print df_processed[missing_dict[x][0]][missing_dict[x][1]]
    



