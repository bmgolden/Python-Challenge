#Importing the Necessary modules
import os 
import csv 

#variable Declaration
total_months = 0
total_profit = 0
profit_losses = []
changes = []
months = []

#Reading the CSV File 
hw_budget_data = os.path.join("Resources", "budget_data.csv")
with open(hw_budget_data, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
#Skipping and Reading the Header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
#For Loop Introduction to Calcualte the Necessary Values while Adding Appropriate Rows to Lists for Future Usage
    for row in csvreader:
           print(row)
           total_months += 1
           total_profit += int(row[1])
           profit_losses.append(int(row[1]))
           months.append(row[0])

#Another For Loop Using Range Technique Calculating the Change Across Each Month 
for i in range(1, len(profit_losses)):
    changes.append(profit_losses[i] - profit_losses[i - 1])

#Calcualting the Average and Rounding
average_change = sum(changes) / len(changes)
average_change_final = round(average_change, 2)

#Finding the Greatest Increase and Decrease
greatest_increase_profits = max(changes)
greatest_decrease_profits = min(changes)

#Extracting the Months with the Greatest Increase and Decrease
greatest_increase_month = months[changes.index(greatest_increase_profits) + 1]
greatest_decrease_month = months[changes.index(greatest_decrease_profits) + 1]

#One F-String to Achieve the Desired Output 
print(f"\nFinancial Analysis\n---------------------\nTotal Months: {total_months}\nTotal: {total_profit}\nAverage Change: {average_change_final}\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")


