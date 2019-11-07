finance = {}

count = 0
high = 0
low = 0
ProfitLoss = 0
date = []
data = []
fields = []
import csv
with open('budget_data.csv',newline = "") as csvFile:
    csvreader = csv.reader(csvFile, delimiter=',')
    fields = next(csvreader)
    #print(f"CSV Header: {fields}")
    for row in csvreader:
        
        #print(row)
        #data = next(csvreader)
        #data.append(row)
        date = row[0]#This is the date from the line we are currently reading
        finance = int(row[1])# This is the profit loss from the line we are currently reading in
        if count == 0: #if count is zero, we want to set our current year to the first year we find
            currentDate = date #setting the date

        if finance > high: #need to find the highest value in all of the data
            high = finance #if we find a higher value, then we set high to that value
        if finance < low: #we to find the highest value in all of the data
            low = finance #if we find a higher value, then we set high to that value

        if date == currentDate: #index 1 of array stores the year value, so we want to add all of the profit loss for a particular year
            ProfitLoss += finance #adding the profit loss together
        else:
            #print('Profit Loss '+ str(ProfitLoss)) #if we reach a new year then we will print the previous year's profit loss
            currentDate = date #setting current year to the new year we have found
            ProfitLoss = finance #setting profit loss to the first profit loss value we found in the new year

        count = count + 1 #track all of the months in the data set

print('High: ' + str(high))

print('Low: ' + str(low))

print ('Total Number of Months: ' + str(count))