import fileinput
from sklearn.linear_model import LogisticRegression

i=-1
unique_player=[]
test_games = []
games_played=[]
training_feature = []
testing_feature = []
training_class = []

##### Extract the training dataset
with open("trainingdata.txt") as f:
    for line in f:
        if i==-1:
            no_games = line
            i=i+1
        else:
            line = line.replace("\n","")
            player_list = line.split(",")
            games_played.append(player_list)
            unique_player.extend(player_list[:-1])

##### Extract the testing dataset
i=-1
for line in fileinput.input():
    if i==-1:
        no_games = line
        i=i+1
    else:
        line = line.replace("\n","")
        player_list = line.split(",")
        test_games.append(player_list)
        
            

unique_player= list(set(unique_player))

count=0
training_set = {}
training_inverse_set = {}
training_features=[]
test_features = []

#### Extract the unique players as features
#### Modify feature into training features
#### convert winning class as 1 and lossing class as -1
#### Add first team as 1 and second team as -1

for x in unique_player:    
    training_set[x]=count
    training_inverse_set[count] = x
    count=count+1

for each_game in games_played:
    game_list=each_game
    each_feature = [0]*(len(unique_player))
    training_game = int(game_list[-1])
    if training_game==1:
        training_class.append(1)
    else:
        training_class.append(-1)
    for i in range(0,len(game_list[:-1])):
        if i<5:
            each_feature[training_set[game_list[i]]]=1
        else:
            each_feature[training_set[game_list[i]]]=-1
    training_feature.append(each_feature)
    

#### Build the model
model = LogisticRegression(C=0.1).fit(training_feature,training_class)

#### Convert the testing feature as training feature
for each_game in test_games:
    game_list=each_game
    each_feature = [0]*(len(unique_player))
    for i in range(0,len(game_list)):
        if i<5:
            each_feature[training_set[game_list[i]]]=1
        else:
            each_feature[training_set[game_list[i]]]=-1
    testing_feature.append(each_feature)
    
#### Predict the result    

prediction = model.predict(testing_feature)
for i in range(0,len(prediction)):
    if prediction[i]==1:
        print 1
    else:
        print 2
