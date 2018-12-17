# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:56:37 2018

"""

import pandas as pd

df = pd.read_csv('parking-violations.csv')

# renaming columns for ease of use
df.rename(columns={'Vehicle Color':'Color','Registration State':'State','Violation Code':'ViolCode', 'Vehicle Make':'Make'}, inplace=True)

# instantiate lists to store various names of colors
WHITE = []
BLACK = []
BROWN = []
GREY = []
RED = []
BLUE = []
GREEN = []
YELLOW = []

# iterate through each color and sort to corresponding bins
for color in df.Color.unique():
    if not (isinstance(color, str)):
        continue
    
    if color.startswith('W'):
        WHITE.append(color)
        continue
    
    if color.startswith('B'):
        if color.startswith('BK') | color.startswith('BLK')  | color.startswith('BLA'):
            BLACK.append(color)
            continue
        if color.startswith('BL'):
            BLUE.append(color)
            continue
        if color.startswith('BUR'):
            RED.append(color)
            continue
        BROWN.append(color)
        continue
    
    if color.startswith('P'):
        BLUE.append(color)
        continue
    
    if color.startswith('G'):
        if color.endswith('Y'):
            GREY.append(color)
            continue
        if color.startswith('GO'):
            YELLOW.append(color)
            continue
        GREEN.append(color)
        continue
    
    if color.startswith('S'):
        GREY.append(color)
        continue    
    
    if color.startswith('R'):
        RED.append(color)
        continue
        
    if color.startswith('Y'):
        YELLOW.append(color)
        continue



# given the lists found above, go through and change in dataframe to new color name
# for example : 'WT' changes to 'WHITE' in csv
def replaceColor(colorlist, colorname):
        df['Color'] = df['Color'].replace(colorlist, colorname)


replaceColor(WHITE,'WHITE')
replaceColor(BLACK,'BLACK')
replaceColor(BROWN,'BROWN')
replaceColor(GREY,'GREY')
replaceColor(GREEN,'GREEN')
replaceColor(RED,'RED')
replaceColor(BLUE,'BLUE')
replaceColor(YELLOW,'YELLOW')


# delete rows that were junk
row2d =[]
colors = ['WHITE', 'BLACK', 'BROWN', 'GREY', 'GREEN', 'RED', 'BLUE', 'YELLOW']
for ind, row in df.iterrows():
    color = row['Color']
    if color not in colors:
        row2d.append(ind)

df = df.drop(df.index[row2d])
#print(df['Color'].unique())




#State plates

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
for ind, row in df.iterrows():
    state = row['State']
    if state not in states:
        # if not from US 50 states, label as FOREIGN
        df.at[ind,'State'] = 'FOREIGN'






#Violation Time

rows2drop = []
for ind, row in df.iterrows():
    
    time = row['Violation Time']
    if isinstance(time, str):
        if time.isnumeric():
            time = int(time)
        else:
            rows2drop.append(ind)
            continue
    
    # sort times into bins of MORNING, AFTERNOON, and NIGHT
    if (time >= 0 and time < 400) or (time >= 2000 and time < 2500):
        df.at[ind,'Violation Time'] = 'NIGHT'
        continue
    if (time >= 400 and time < 1200):
        df.at[ind,'Violation Time'] = 'MORNING'
        continue
    if (time >= 1200 and time < 2000):
        df.at[ind,'Violation Time'] = 'AFTERNOON'
        continue
    
    #didn't fall into category, must be bad number
    rows2drop.append(ind)
    
    
    
# throw away numbers that didn't sort to any bin
df = df.drop(df.index[rows2drop])
print(df)



# output dataframe to new csv file
df.to_csv('parkingAltered.csv')
    
            