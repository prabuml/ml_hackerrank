import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import fileinput

#######Extract the Testing data
i=-1
testing_data=[]
for line in fileinput.input():
    if i==-1:
        no_test=int(line.split(" ")[0])
        i=i+1
    else:
        testing_data.append(json.loads(line))
        
testing_feature= [x['question'].lower() + " " + x['excerpt'].lower() for x in testing_data]

#######Extract the Training data
data = []
with open('training.json') as f:
    for line in f:
        data.append(json.loads(line))
        
training_feature =[x['question'].lower() + " " + x['excerpt'].lower() for x in data[1:]]
training_topics = [x['topic'] for x in data[1:]]


#######Extract the unique topics and assign a class i.e number corresponding to each topic
unique_topics =list(set(training_topics))
training_set = {}
training_inverse_set = {}
count=0
for x in unique_topics:
    count=count+1
    training_set[x]=count
    training_inverse_set[count] = x
training_class = [training_set[x] for x in training_topics]

#######Build the Model    
max_range=1
vectorizer = TfidfVectorizer(max_df=1.0, ngram_range=(1,max_range),stop_words='english', use_idf='True')
vectorized_feature = vectorizer.fit_transform(training_feature)
model = MultinomialNB().fit(vectorized_feature, training_class)

#######Predict the Output
vectorized_feature_test = vectorizer.transform(testing_feature)
prediction = model.predict(vectorized_feature_test)
for each_prediction in prediction:
    print training_inverse_set[each_prediction]
