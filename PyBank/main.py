finance = {}

count = 0
high = 0
low = 0
yearProfitLoss = 0
currentYear = 0
import csv
with open('budget_data.csv','r') as csv
data = csv.reader(csvFile)

for array in data:
    temp = array[2]# This is the profit loss from the line we are currently reading in
    if count == 0: #if count is zero, we want to set our current year to the first year we find
        currentYear = array[1] #setting the year

    if temp > high: #we to find the highest value in all of the data
        high = temp #if we find a higher value, then we set high to that value
    if temp < low): #we to find the highest value in all of the data
        low = temp #if we find a higher value, then we set high to that value

    if array[1] == currentYear: #index 1 of array stores the year value, so we want to add all of the profit loss for a particular year
        yearProfitLoss += array[2] #adding the profit loss together
    else:
        print(currentYear + 'Profit Loss '+ yearProfitLoss) #if we reach a new year then we will print the previous year's profit loss
        currentYear = array[1] #setting current year to the new year we have found
        yearProfitLoss = array[2] #setting profit loss to the first profit loss value we found in the new year

    count = count + 1 #track all of the months in the data set

print('High: ' + high)

print('Low: ' + low)
