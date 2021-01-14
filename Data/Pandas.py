#Regulation of Safety 
'''
1. when turning left or right acceleration must be negative
2. no fuel under 4 
3. rate the driving according to the mean. if its upper the mean(tend to danger, dangerous), when below(below normal)
4. You can't use left and right together'
'''

import pandas as pd
#read file
data = pd.read_excel('data.xlsx')
data = data.loc[data.Fuel >= 4] #no fuel under 4 
data = data.loc[(data.Left == True) & (data.Right == True)] #you can't use left and right 
mean_of_data = data.Acceleration.mean() #mean of the acceleration
median_of_data = data.Acceleration.median() #median of the acceleration
#data.set_index("Time")

data_process = True
i = 0
while data_process:
    acc = data['Acceleration'][i]
    fuel = data['Fuel'][i]
    battery = data['Battery'][i]
    belt= data['Set Belt'][i]
    alart = data['Alart'][i]
    engine = data['Engine'][i]
    left = data['Left'][i]
    right = data['Right'][i]


    i +=1
    print(acc)
    
#print(data)   
# I may set an index
'''
reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
for the sake of selection

n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

'''    
    
    
