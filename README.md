# CSCI-4502-Group-Project
Group Project for CSCI 4502

Team Members:

Cody Hegwer
Jeff LaPrade
Adam Grabowski

Description:

In this report, we summarize our findings for applying the Apriori algorithm and Bayesian classification to a data set containing records for parking violations issued in New York in recent times. 

Questions:

The main questions we wish to address are: “Is there a clearly identifiable trend relating attributes of our data that could be used to avoid receiving traffic violations?” and “Among any trends we can identify, are those trends consistent throughout the city or does each area of the city have their own patterns of violations?”

Although we were not able to directly answer the second question regarding correlating aspects of violations to different parts of the city, we were able to find some information to help answer the first question. Many of the attributes concerning the violations were not very correlated and we believe that they are not strong predictors of whether or not a violation will occur. Additionally, only a few attributes were found to be in frequent itemsets with strong support and confidence. These findings primarily indicate that certain violations were considerably more likely to happen at certain times of day. In particular:

    Street Cleaning: Morning
    Parking in Excess of Allowed Time: Afternoon
    Failing to Show Receipt: Afternoon
    General Parking Violation: Morning

Application:

Applying these findings, we can suggest certain methods for traversing the city. Since it is shown that it is far more likely to receive a general parking violation in the morning and parking in excess of allowed time violation in the afternoon, it makes sense to ensure that one is parked legitimately and pays for their parking in the morning as the chances of evading a violation are slim then. However, by afternoon, it can be considered much safer to move your vehicle to another location and either not pay for the parking, or start the meter then. Since it is so much less common for general parking violations to be issued in the afternoon, you could take the safe bet of not receiving a violation then when parking illegitimately. Additionally, if you wish to play it safer and still park legitimately, you could expect to feed a parking meter in the afternoon and then not reset it since evening and night excess of allowed time violations are rare and they are only commonly issued in the afternoon. 


Running Apriori Algorithm in notebook:

After experimenting with building our own Apriori algorithm, we came across a well known apriori module for python and decided that would be sufficent for our needs. The module only accepts data as input as a list of lists so we had to transform the data from the CSV format to a format the module would accept. 

Included in the notebook at many examples of running the algorithm on different subsets of the data with different support and confidence requirements. If you wish to rererun with different values, just change them and reload the cell.

Running Bayesian Classifers:

There are three BC python files, 'BCtime.py', 'BCcolor.py', and 'BCviolation.py'. They should be able to run from command line with ex: "python3 BCtime.py". Otherwise just run the scripts in a python 3 editor. At the bottom of each script is a call to the function "Bayes()". It takes 3 arguments that are different for each script. (essentially the 4 main attributes minus the one thats being predicted). What is returned is the top three predicted values for the given permutation you have run.

Tableau:

Download the most recent Tableau if you would like to view the visualizations. Download from our Github repository "TABLEAU-VIZ.twb". The visualiztions utilize parkingAltered.csv so that will need to be loaded into Tableau as well.


Link to Video Presentation:
https://drive.google.com/file/d/1P50u08K0x_3RDAdeduiwWNrU1O8nZNrT/view?ts=5c16f020

Link to Final Report:
https://docs.google.com/document/d/1EkxX8qa-zPmT-53yTtC_LlZCpixj9cGI0zZ854i0upw/edit
