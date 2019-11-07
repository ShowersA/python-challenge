import os
import csv
	

budget_file = os.path.join("budget_data.csv")


monthsCount = 0
ProfitLoss = 0
value = 0
profitChange = 0
dates = []
profits = []

with open(budget_file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

    row = next(csvreader)
    monthsCount += 1
    ProfitLoss += int(row[1])
    value = int(row[1])
    
    for row in csvreader:
        dates.append(row[0])
        
        profitChange = int(row[1])-value
        profits.append(profitChange)
        value = int(row[1])
        
        monthsCount += 1
        ProfitLoss = ProfitLoss + int(row[1])

    greatest_inc = max(profits)
    greatest_num = profits.index(greatest_inc)
    greatest_date = dates[greatest_num]
 
    greatest_dec = min(profits)
    worst_num = profits.index(greatest_dec)
    worst_date = dates[worst_num]
    avg_change = sum(profits)/len(profits)
    


print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(monthsCount))
print("Total: $" + str(ProfitLoss))
print("Average Change: $" + str(round(avg_change,2)))
print("Greatest Increase in Profits: " + greatest_date +  " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + worst_date + " ($" + str(greatest_dec) + ")")

output = open("pybank_results.txt", "w")

output.write("Financial Analysis\n")
output.write("---------------------\n")
output.write("Total Months: " + str(monthsCount))
output.write("\nTotal: $" + str(ProfitLoss))
output.write("\nAverage Change: $" + str(round(avg_change,2)))
output.write("\nGreatest Increase in Profits: " + greatest_date +  " ($" + str(greatest_inc) + ")")
output.write("\nGreatest Decrease in Profits: " + worst_date + " ($" + str(greatest_dec) + ")")

output.close()