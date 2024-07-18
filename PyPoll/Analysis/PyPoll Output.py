import os
import csv

totalvotes = 0
totalvotecounts = {}
final_output = []

csv_election_data = os.path.join('Resources', 'election_data.csv')
with open(csv_election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        totalvotes += 1
        candidates = row[2].strip()
        if candidates in totalvotecounts:
            totalvotecounts[candidates] += 1
        else:
            totalvotecounts[candidates] = 1

final_output.append("Election Results")
final_output.append("---------------")
final_output.append(f"Total Votes: {totalvotes}")
final_output.append("---------------")
    
for candidates, count in totalvotecounts.items():
    percentage = round(((count / totalvotes) * 100), 3)
    final_output.append(f"{candidates}: {percentage}% ({count})")

win = max(totalvotecounts, key=totalvotecounts.get)
final_output.append("---------------")
final_output.append(f"Winner: {win}")
final_output.append("---------------")

results_report = os.path.join("PyPoll", "Analysis", "Election_Results.txt")
with open(results_report, "w") as file:
    for line in final_output:
        file.write(line + "\n")