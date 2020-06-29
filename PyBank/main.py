# The following code allowed us to locate and create the files that we needed for this assignment, namely, csv and text ones. 
import os
import csv

# The following code allowed us to locate our budget_data.csv excel file.
csvpath = os.path.join('/Users/azpunit/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

# The following code allowed us to store the header row into a row and the total number of months into a variable.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    Total_Months = len(list(csvreader))

# The following code allowed us to create all the lists that helped us store our values found into variables.
Total_Profit_List = []
Previous = []
Next_List = []
Change = []
Dates = []

# The following code allowed us to store the total profit into a variable.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        Total_Profit_List.append(int(row[1]))
Total_Profit = sum(Total_Profit_List)

# The following code allowed us to store the average change, the greatest increase in profits and the greatest decrease in profits
# into variables.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        Previous.append(int(row[1]))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    row = next(csvreader)
    for row in csvreader:
        Next_List.append(int(row[1]))

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    Zip_Object = zip(Previous, Next_List)
    for Previous_i, Next_List_i in Zip_Object:
        Change.append(Next_List_i - Previous_i)  

Average_Change = round(sum(Change)/len(Change), 2)
Greatest_Percent_Increase = max(Change)
Greatest_Percent_Decrease = min(Change)

# The following code allowed us to store the dates of the greatest increase and decrease in profits into variables. 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        Dates.append(str(row[0]))

Raw_Greatest_Increase_In_Profits_Date = str(Dates[25])
First_Formatter = Raw_Greatest_Increase_In_Profits_Date.replace("12-","")
Second_Formatter = Raw_Greatest_Increase_In_Profits_Date.replace("12-Feb","-2012")
Final_Greatest_Increase_In_Profits_Date = str(First_Formatter) + str(Second_Formatter)

Raw_Greatest_Decrease_In_Profits_Date = str(Dates[44])
Third_Formatter = Raw_Greatest_Decrease_In_Profits_Date.replace("13-","")
Fourth_Formatter = Raw_Greatest_Decrease_In_Profits_Date.replace("13-Sep","-2013")
Final_Greatest_Decrease_In_Profits_Date = str(Third_Formatter) + str(Fourth_Formatter)

#  The following code allowed us to print our final text, including all the previously stored variables, similarly to the analysis
# provided to us on our homework prompt. 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Profit}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Final_Greatest_Increase_In_Profits_Date} (${Greatest_Percent_Increase})")
print(f"Greatest Decrease in Profits: {Final_Greatest_Decrease_In_Profits_Date} (${Greatest_Percent_Decrease})")

# The following code allowed us to create our Results.txt file.
Results = os.path.join('/Users/azpunit/Desktop/python-challenge/PyBank/Analysis/Results.txt')

# The following code allowed us to write exactly the same text that we previously printed in terminal in the Results.txt file. 
with open(Results, 'w') as text:    
    text.write("Financial Analysis" + str("\n"))
    text.write("----------------------------" + str("\n"))
    text.write(f"Total Months: {Total_Months}\n")
    text.write(f"Total: ${Total_Profit}\n")
    text.write(f"Average Change: ${Average_Change}\n")
    text.write(f"Greatest Increase in Profits: {Final_Greatest_Increase_In_Profits_Date} (${Greatest_Percent_Increase})\n")
    text.write(f"Greatest Decrease in Profits: {Final_Greatest_Decrease_In_Profits_Date} (${Greatest_Percent_Decrease})\n")
