#Importing the Necessary Modules
import os
import csv
#Variable Declaration
totalvotes = 0
totalvotecounts = {}
#Readnig the CSV File
csv_election_data = os.path.join('Resources', 'election_data.csv')
with open(csv_election_data) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
#Skipping and Reading the Header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
 #For Loop Introduction to Calcualate Necessary Values
    for row in csvreader:
        totalvotes += 1
        candidates = row[2].strip()
 #Conditional Use To Tally Up the Votes
        if candidates in totalvotecounts:
            totalvotecounts[candidates] += 1
        else:
            totalvotecounts[candidates] = 1
#Adding the Sums to the Total Vote Count Dictionary
    candidate_list = list(totalvotecounts.keys())
#Printing the Output with the use of F-String
    print(f"Election Results\n-----------------\nTotal Votes: {totalvotes}\n-----------------")
#Final For Loop to Calculate the Necessary Percentages
    for candidates, count in totalvotecounts.items():
        percentage = round(((count / totalvotes) * 100), 3)
        print(f"{candidates}: {percentage:}% ({count})")
#Declaring the Winner and Printing it Out 
    winner = max(totalvotecounts, key=totalvotecounts.get)
    print(f"---------------------\nWinner: {winner}\n---------------------")
       

