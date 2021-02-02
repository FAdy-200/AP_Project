The following project is done by :
Abdelrahman Khaled  		120180041
Fadi Alahmad Alomar	    	120180049
Mennatullah Abdelrahman 	120180009

it a dashboard with an alert system that alerts the user of unsafe driving
it can operate on two modes:
1. user input mode
    which takes all the needed data from the keyboard to simulate realtime analysis
2. file input mode
    which take the data from a .csv file to be used in the analysis

the code has an acceleration attribute that has the last 100 recorded acceleration. if the total samples were less
than 100 it takes all of them until they reach a 100 them it starts keeping only the last 100

RUNNING INSTRUCTIONS:
1. the code needs to be in folder that has a subfolder called Data
2. the Data subfolder needs to have the needed images and sensor data
3. run DashBoard.py
