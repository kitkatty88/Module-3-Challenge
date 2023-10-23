#Importing modules/libraries
import os
import csv

#Loading Files
budget_data = os.path.join("C:\\Users\\Class\\hw3\\PyBank\\Resources\\budget_data.csv")
output_data = os.path.join("C:\\Users\\Class\\hw3\\PyBank\\Analysis\\PyBank_analysis.txt")

#Defining Parameters
dates = []
profits = []
total_months = 0
total_net = 0
value = 0
change = 0

#Reading CSV and converting into a list
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

 #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    value = int(first_row[1])
    
    #For all following rows 
    for row in csvreader:
        # Keeping track of the months
        dates.append(row[0])
        
        # Calculate the change
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Calculating Total
        total_months += 1
        total_net = total_net + int(row[1])

    #Greatest increase
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change"
    avg_change = sum(profits)/len(profits)
    

#Checking information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporting to text file
output = open("C:\\Users\\Class\\hw3\\PyBank\\Analysis\\PyBank_analysis.txt", "w")

line1 = "Financial Analysis"
line2 = "-------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_net)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))