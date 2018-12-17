# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:08:32 2018

"""

import pandas as pd

df = pd.read_csv('parkingAltered.csv')

#This version predicts the color of vehicle given state license plate, violation code, and time  
   
   
def Bayes(state, vcode, time):
    
    #instantiate counting variables
    totalN = 0
    
    black = 0
    grey = 0
    brown = 0
    white = 0
    b = 0 #blue
    g = 0 #green
    r = 0 #red
    y = 0 #yellow
    
    stategivblack = 0
    stategivgrey = 0
    stategivbrown = 0
    stategivwhite = 0
    stategivb = 0
    stategivg = 0
    stategivr = 0
    stategivy = 0
    
    vcodegivblack = 0
    vcodegivgrey = 0
    vcodegivbrown = 0
    vcodegivwhite = 0
    vcodegivb = 0
    vcodegivg = 0
    vcodegivr = 0
    vcodegivy = 0
    
    timegivblack = 0
    timegivgrey = 0
    timegivbrown = 0
    timegivwhite = 0
    timegivb = 0
    timegivg = 0
    timegivr = 0
    timegivy = 0

    
    for ind, row in df.iterrows():
        
        totalN += 1
        
        color = row['Color']
        statetest = row['State']
        vcodetest = row['ViolCode']
        timetest = row['Violation Time']
        
        
        #increment variables depending on matching attributes
        
        if color == 'BLACK':
            black += 1
            if statetest == state:
                stategivblack += 1
            if vcodetest == vcode:
                vcodegivblack += 1
            if timetest == time:
                timegivblack += 1
            continue

                
        if color == 'GREY':
            grey += 1
            if statetest == state:
                stategivgrey += 1
            if vcodetest == vcode:
                vcodegivgrey += 1
            if timetest == time:
                timegivgrey += 1
            continue
        
        
        if color == 'BROWN':
            brown += 1
            if statetest == state:
                stategivbrown += 1
            if vcodetest == vcode:
                vcodegivbrown += 1
            if timetest == time:
                timegivbrown += 1
            continue
        
        
        if color == 'WHITE':
            white += 1
            if statetest == state:
                stategivwhite += 1
            if vcodetest == vcode:
                vcodegivwhite += 1
            if timetest == time:
                timegivwhite += 1
            continue

            
        if color == 'BLUE':
            b += 1
            if statetest == state:
                stategivb += 1
            if vcodetest == vcode:
                vcodegivb += 1
            if timetest == time:
                timegivb += 1
            continue

            
        if color == 'GREEN':
            g += 1
            if statetest == state:
                stategivg += 1
            if vcodetest == vcode:
                vcodegivg += 1
            if timetest == time:
                timegivg += 1
            continue
        
        
        if color == 'RED':
            r += 1
            if statetest == state:
                stategivr += 1
            if vcodetest == vcode:
                vcodegivr += 1
            if timetest == time:
                timegivr += 1
            continue
        
        if color == 'YELLOW':
            y += 1
            if statetest == state:
                stategivy += 1
            if vcodetest == vcode:
                vcodegivy += 1
            if timetest == time:
                timegivy += 1
            continue
    
    # base percentages of colors
    black = black/totalN
    grey = grey/totalN
    brown = brown/totalN
    white = white/totalN
    b = b/totalN
    g = g/totalN
    r = r/totalN
    y = y/totalN
    
    # given percentages per color
    givblack = (stategivblack/totalN) * (vcodegivblack/totalN) * (timegivblack/totalN)
    givgrey = (stategivgrey/totalN) * (vcodegivgrey/totalN) * (timegivgrey/totalN)
    givbrown = (stategivbrown/totalN) * (vcodegivbrown/totalN) * (timegivbrown/totalN)
    givwhite = (stategivwhite/totalN) * (vcodegivwhite/totalN) * (timegivwhite/totalN)
    givb = (stategivb/totalN) * (vcodegivb/totalN) * (timegivb/totalN)
    givg = (stategivg/totalN) * (vcodegivg/totalN) * (timegivg/totalN)
    givr = (stategivr/totalN) * (vcodegivr/totalN) * (timegivr/totalN)
    givy = (stategivy/totalN) * (vcodegivy/totalN) * (timegivy/totalN)
    
    # find probabilites
    probBlack = givblack * black
    probGrey = givgrey * grey
    probBrown = givbrown * brown
    probWhite = givwhite * white
    probBlue = givb * b
    probGreen = givg * g
    probRed = givr * r
    probYellow = givy * y
    
    print('Black:', probBlack, '\nGrey:', probGrey, '\nBrown:', probBrown, '\nWhite:', probWhite, '\nBlue:', probBlue, '\nGreen:', probGreen, '\nRed:', probRed, '\nYellow:', probYellow)
    
    return

Bayes('NY', 20, 'NIGHT')
