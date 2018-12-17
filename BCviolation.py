# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:03:13 2018

@author: Cody
"""

import pandas as pd

df = pd.read_csv('parkingAltered.csv')

#This version predicts the violation code of vehicle given state license plate, color, and time  

#   VIOLARRAY USED IN FUNCTION BELOW
#
#   viol code  |  # of occurence  |  stategivencode#  |   colorgivencode#   |  timegivencode#| probability of set X | Prob of violation code given set X|
#   ____________________________________________________________________________________________________________________________________________________|
#       0      |       24626      |       124124      |         1414        |       200000   |         tbd          |                   tbd             |
#       1      |       14426      |       124144      |         124         |       20       |         tbd          |                   tbd             |
#      ...
#       99
        
   
def Bayes(state, time, color):
    
    totalN = 0
    rows = 100
    columns = 7
    violArray = [[0 for x in range(columns)] for y in range(rows)] 
    
    for i in range(rows):
        violArray[i][0] = i

    
    for ind, row in df.iterrows():
        
        
        totalN += 1
        
        colortest = row['Color']
        statetest = row['State']
        vcode = row['ViolCode']
        timetest = row['Violation Time']
        
        
        
        #increment counters in 2D array
        
        violArray[vcode][1] += 1        
        
        if statetest == state:
            violArray[vcode][2] += 1
        if colortest == color:
            violArray[vcode][3] += 1
        if timetest == time:
            violArray[vcode][4] += 1

    
    
    # Find the probable violation codes
    fstMax = 0
    sndMax = 0
    trdMax = 0
  
    # divide by n to find probabilities and given probabilities
    
    for i in range(rows):
        
        violArray[i][1] = violArray[i][1] / totalN #probability of violation code
        
        violArray[i][5] = (violArray[i][2] / totalN) * (violArray[i][3] / totalN) * (violArray[i][4] / totalN) #probability of set X given violation code
        
        violArray[i][6] = violArray[i][1] * violArray[i][5] # find overall probability
        
        # find largest probability
        if violArray[i][6] > violArray[fstMax][6]:
            trdMax = sndMax
            sndMax = fstMax
            fstMax = i
            continue
        
        # find second largest probability
        if violArray[i][6] > violArray[sndMax][6]:
            trdMax = sndMax
            sndMax = i
            continue
        
        # find third largest probability
        if violArray[i][6] > violArray[trdMax][6]:
            trdMax = i
            continue
            
    # Violation code with corresponding probability
    print( fstMax, " ", violArray[fstMax][6], "\n", sndMax, " ", violArray[sndMax][6], "\n", trdMax,  " ", violArray[trdMax][6])
    
    
    return



Bayes('NJ', 'NIGHT', 'WHITE')
