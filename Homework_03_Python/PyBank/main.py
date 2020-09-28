import os
import csv
#file path
financial = os.path.join( "Resources", "budget_data.csv")

#creat list 

months = []
profit = []
monthly_change = []
#read csv and set header
with open(financial) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvfile)
    
#read through csv and update list
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
        
    for i in range(len(months)-1):
            monthly_change.append(int(profit[i+1])-int(profit[i]))
#creat variable for totals
total_months = len(months)
total_profit = sum(profit)
average= float(round((sum(monthly_change)/len(monthly_change)),2))

#get month index base on greatest increase/decrease amount
greatesincrease_month_index = monthly_change.index(max(monthly_change)) + 1
greatesdecrease_month_index = monthly_change.index(min(monthly_change)) + 1
greatesincreasemonth = months[greatesincrease_month_index]
greatesdecreasemonth = months[greatesdecrease_month_index]

#print resultß

print("Financial Analysis")
print("------------------------")
print(f'Total Months: {total_months}')
print(f'Total: $ {total_profit}')
print(f'Average Change: $ {average}')
print(f'Greatest Increase in Profits: {greatesincreasemonth} ($ {max(monthly_change)} )')
print(f'Greatest Decrease in Profits: {greatesdecreasemonth} ($ {min(monthly_change)} )')

#output text file
output_path = os.path.join("result")

with open(output_path,'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------\n")
    textfile.write(f'Total Months: {total_months}\n')
    textfile.write(f'Total: $ {total_profit}\n')
    textfile.write(f'Average Change: $ {average}\n')
    textfile.write(f'Greatest Increase in Profits: {greatesincreasemonth} ($ {max(monthly_change)} )\n')
    textfile.write(f'Greatest Decrease in Profits: {greatesdecreasemonth} ($ {min(monthly_change)} )\n')