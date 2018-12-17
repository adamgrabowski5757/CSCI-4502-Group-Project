# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:03:26 2018

@author: Cody
"""


import pandas as pd

df = pd.read_csv('parkingAltered.csv')

#This version predicts the color of vehicle given state license plate, violation code, and time  
   
   
def Bayes(state, vcode, color):
    totalN = 0
    
    morn = 0
    noon = 0
    night = 0

    
    stategivmorn = 0
    stategivnoon = 0
    stategivnight = 0

    
    vcodegivmorn = 0
    vcodegivnoon = 0
    vcodegivnight = 0

    
    colorgivmorn = 0
    colorgivnoon = 0
    colorgivnight = 0


    
    for ind, row in df.iterrows():
        
        totalN += 1
        
        colortest = row['Color']
        statetest = row['State']
        vcodetest = row['ViolCode']
        time = row['Violation Time']
        
        if time == 'MORNING':
            morn += 1
            if statetest == state:
                stategivmorn += 1
            if vcodetest == vcode:
                vcodegivmorn += 1
            if colortest == color:
                colorgivmorn += 1
            continue

                
        if time == 'AFTERNOON':
            noon += 1
            if statetest == state:
                stategivnoon += 1
            if vcodetest == vcode:
                vcodegivnoon += 1
            if colortest == color:
                colorgivnoon += 1
            continue
        
        
        if time == 'NIGHT':
            night += 1
            if statetest == state:
                stategivnight += 1
            if vcodetest == vcode:
                vcodegivnight += 1
            if colortest == color:
                colorgivnight += 1
            continue
    
    
    # base percentages of times
    morn = morn/totalN
    noon = noon/totalN
    night = night/totalN

    
    # given percentages per times
    givmorn = (stategivmorn/totalN) * (vcodegivmorn/totalN) * (colorgivmorn/totalN)
    givnoon = (stategivnoon/totalN) * (vcodegivnoon/totalN) * (colorgivnoon/totalN)
    givnight = (stategivnight/totalN) * (vcodegivnight/totalN) * (colorgivnight/totalN)

    # find probabilities
    probMorn = givmorn * morn
    probNoon = givnoon * noon
    probNight = givnight * night

    
    print('Morning:', probMorn, '\nNoon:', probNoon, '\nNight:', probNight)
    
    return

Bayes('NJ', 20, 'WHITE')


