import fileinput

#######Extract the Testing data
for line in fileinput.input():
    testing_data=float(line)
    
####Based on training data, the rule is inferred as below

if testing_data>4:
    print 8
else:
    print 2*testing_data
