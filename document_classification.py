
import fileinput
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

#######Extract the Training data
data = []
with open("trainingdata.txt") as f:  
    for line in f:
        data.append(line)
training_class = [x.split(" ")[0] for x in data[1:]]
training_text = [" ".join(x.split(" ")[1:]).lower() for x in data[1:]]

#######Extract the Testing data
i=-1
testing_text=[]
for line in fileinput.input():
    if i==-1:
        no_test=int(line.split(" ")[0])
        i=i+1
    else:
        testing_text.append(line.lower())

#######Build the Model            
max_range=1
vectorizer = TfidfVectorizer(ngram_range=(1,max_range),max_df=0.9, stop_words='english', use_idf='True')
vectorized_feature  = vectorizer.fit_transform(training_text)
clf = SGDClassifier().fit(vectorized_feature, training_class)

#######Predict the Output
vectorized_feature_test  = vectorizer.transform(testing_text)
prediction = clf.predict(vectorized_feature_test )
for each_prediction in prediction:
    print each_prediction

