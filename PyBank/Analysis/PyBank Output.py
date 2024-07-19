import os 
import csv 

total_months = 0
total_profit = 0
profit_losses = []
changes = []
months = []
final_output = []

hw_budget_data = os.path.join("Resources", "budget_data.csv")
with open(hw_budget_data, "r") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
           print(row)
           total_months += 1
           total_profit += int(row[1])
           profit_losses.append(int(row[1]))
           months.append(row[0])

for i in range(1, len(profit_losses)):
    changes.append(profit_losses[i] - profit_losses[i - 1])

average_change = sum(changes) / len(changes)
average_change_final = round(average_change, 2)
greatest_increase_profits = max(changes)
greatest_decrease_profits = min(changes)

greatest_increase_month = months[changes.index(greatest_increase_profits) + 1]
greatest_decrease_month = months[changes.index(greatest_decrease_profits) + 1]

final_output.append("Financial Analysis")
final_output.append("---------------")
final_output.append(f"Total Months: {total_months}")
final_output.append(f"Total Profit: ${total_profit}")
final_output.append(f"Average Change: ${average_change_final}")
final_output.append(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profits})")
final_output.append(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profits})")

results_report = os.path.join("PyBank", "Analysis", "Financial_Analysis.txt")
with open(results_report, "w") as file:
    for line in final_output:
        file.write(line + "\n")
