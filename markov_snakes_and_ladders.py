import fileinput
import numpy
from numpy.linalg import inv
import random


####Function to roll a die
def roll_dice(dice_probability_list):
    #### Assign a random value between 0 and 1
    rand_roll = random.random()
    #### Initial output probability as 0
    output_probability = 0
    #### Initial die value as 1
    die_value = 1
    #### Repeatly add the probability to output probability untill reaches rand_roll
    ##### return corresponding die value
    for each_probability in dice_probability_list:
        output_probability += each_probability
        if rand_roll < output_probability:
            return die_value
        die_value+=1

#### Extract different games input   
i=-1
different_games={}
for line in fileinput.input():
    if i==-1:
        no_games= int(line.split(" ")[0])
        i=i+1
    elif i%4==0:
        different_games[i/4]={}
        different_games[i/4]['die_probability']=[float(x) for x in line.split(",")]
        i=i+1
    elif i%4==1:
        i=i+1
    elif i%4==2:     
        change_state = [x.replace("\n","") for x in line.split(" ")]
        different_games[i/4]['change']={}
        for x in change_state:
            different_games[i/4]['change'][int(x.split(',')[0])]=int(x.split(',')[1])
        i=i+1
    elif i%4==3:
        change_state= [x.replace("\n","") for x in line.split(" ")]
        for x in change_state:
            different_games[i/4]['change'][int(x.split(',')[0])] = int(x.split(',')[1])
        i=i+1    
   

n=100
m=6

#### For each game played , 
####     Roll the dice and move to next step
####     Repeat the steps until you reach 100 or number of steps greater than 10000  
#### 
#### Take average of all the each_game_played as the final output 
for each_game in different_games:    
    count=0
    position= 1
    count_list=[]
    for each_game_played in range(0,10000):
        count=1
        position=1
        new_position=0
        while(count<1000):
            new_position = roll_dice(different_games[each_game]['die_probability'])
            if int(new_position + position) in different_games[each_game]['change'].keys():
                new_position = different_games[each_game]['change'][new_position+position]
            else:
                new_position = new_position + position 
            if new_position==100:
                break
            if new_position<101:
                position = new_position
            count=count+1    
        if new_position==100:
            count_list.append(count)
            
    print sum(count_list)/10000   
    
        
