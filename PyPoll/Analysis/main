#Importing modules/libraries
import os
import csv

#Loading Files
election_data = os.path.join("C:\\Users\\Class\\hw3\\PyPoll\\Resources\\election_data.csv")
output_data = os.path.join("C:\\Users\\Class\\hw3\\PyPoll\\Analysis\\PyPoll_analysis.txt")

#Defining Parameters
candidates = []
total_votes = 0
count_votes = []
percent_votes = []

#Reading CSV and converting into a list
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
#For all following rows
    for row in csvreader:
        total_votes += 1 
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            count_votes.append(1)
        else:
            index = candidates.index(row[2])
            count_votes[index] += 1
            
    # Add to percent_votes list 
    for votes in count_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Find winner
    winner = max(count_votes)
    index = count_votes.index(winner)
    winning_candidate = candidates[index]

# Checking results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(count_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Exporting to text file
output = open("C:\\Users\\Class\\hw3\\PyPoll\\Analysis\\PyPoll_analysis.txt"
, "w")

line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("-------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(count_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "-------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "-------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))