    #import module os
import os

#print(os.getcwd() + "\n")

#import csv
import csv


csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

#open csv path and reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
   
    csv_header = next(csvreader)
    print(csv_header)

    Date = []
    Profit_Losses = []
    Difference = []

    for row in csvreader:

        Profit_Losses.append(float(row[1]))
        Date.append(row[0])
    for row in range(1,len(Profit_Losses)):
        Difference.append(Profit_Losses[row]-Profit_Losses[row-1])
        avg_change = sum(Difference)/len(Difference)
        greatest_increase = max(Difference)
        greatest_decrease = min(Difference)
    
    
Total = "${:,.2f}".format(sum(Profit_Losses))
print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {len(Date)}')
print(f'Total: {Total}')
print(f'Average Change: {avg_change}')
print(f'Greatest Increase in Profits: {greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease}')



   
    


   

