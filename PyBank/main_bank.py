#import module os
import os



#import csv
import csv

#create path to files
csvpath = os.path.join("Resources","budget_data.csv")
csv_out = os.path.join("Analysis","Budget_Data_Analysis.txt")

#open csv path and reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
 
 #check headers of columns  
    csv_header = next(csvreader)
    print(csv_header)

#creat empty lists for each column to put data into
    Date = []
    Profit_Losses = []
    Difference = []

#loop through data to put the data into either profic/losses or date  
    for row in csvreader:
        
        Profit_Losses.append(float(row[1]))
        Date.append(row[0])

#loop through created profit/losses list to find difference between consecutive values to find average, greatest increase,
#  and greatest difference
    for row in range(0,len(Profit_Losses)):
        Difference.append(Profit_Losses[row]-Profit_Losses[row-1])
        avg_change = sum(Difference)/len(Difference)
        greatest_increase = max(Difference)   
        greatest_decrease = min(Difference)

    #formatting of obtained values to currency format with two decimal places
        avg = "${:,.2f}".format(avg_change)
        increase = "${:,.2f}".format(greatest_increase)
        decrease = "${:,.2f}".format(greatest_decrease)

    #finds corresponding date for the greatees incease and greatest decrease values
        increase_month = Date[Difference.index(greatest_increase)]
        decrease_month = Date[Difference.index(greatest_decrease)]
    
    #format profit/losses value to to currency format with two decimal places
    Total = "${:,.2f}".format(sum(Profit_Losses))
    print("Financial Analysis")
    print("-------------------------")
    print(f'Total Months: {len(Date)}')
    print(f'Total: {Total}')
    print(f'Average Change: {avg}')
    print(f'Greatest Increase in Profits:{increase_month} ({increase})')
    print(f'Greatest Decrease in Profits: {decrease_month}({decrease})')
  
#writes new csv in designated folder
with open(csv_out,'w') as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------\n")
    f.write(f"Total Months: {len(Date)}\n")
    f.write(f'Total: {Total}\n')
    f.write(f'Average Change: {avg}\n')
    f.write(f'Greatest Increase in Profits:{increase_month} ({increase})\n')
    f.write(f'Greatest Decrease in Profits: {decrease_month}({decrease})\n')


   
    


   

