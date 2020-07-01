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

# The following code allowed us to create some lists and values that helped us store the results that we found into variables.
Total_Profit_List = []
Previous = []
Next_List = []
Change = []
Dates = []
Greatest_Increase = float("-inf")
Greatest_Decrease = float("inf")

# The following code allowed us to store the total profit into a variable.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        Total_Profit_List.append(int(row[1]))
Total_Profit = sum(Total_Profit_List)

# The following code allowed us to store the average change. Also, it allowed us to store the greatest increase in profits and 
# the greatest decrease in profits with the dates when they occured into variables.
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
    for row in csvreader:
        Dates.append(str(row[0]))  

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    Zip_Object = zip(Previous, Next_List, Dates[1:])
    for Previous_i, Next_List_i, Dates_i in Zip_Object:
        Monthly_Change = Next_List_i - Previous_i
        Change.append(Monthly_Change)
        if (Monthly_Change > Greatest_Increase):
            Greatest_Increase = Monthly_Change
            Raw_Greatest_Increase_In_Profits_Date = Dates_i
        if (Monthly_Change < Greatest_Decrease):
            Greatest_Decrease = Monthly_Change
            Raw_Greatest_Decrease_In_Profits_Date = Dates_i

Average_Change = round(sum(Change)/len(Change), 2)
Greatest_Increase_In_Profits = max(Change)
Greatest_Decrease_In_Profits = min(Change)

Raw_Greatest_Increase_In_Profits_Date.split("-")
First_String_Formatting = str(Raw_Greatest_Increase_In_Profits_Date[3]) + str(Raw_Greatest_Increase_In_Profits_Date[4])
Second_String_Formatting = str(Raw_Greatest_Increase_In_Profits_Date[5])+ str(Raw_Greatest_Increase_In_Profits_Date[2]) + "20"
Third_String_Formatting = str(Raw_Greatest_Increase_In_Profits_Date[0]) + str(Raw_Greatest_Increase_In_Profits_Date[1])
Final_Greatest_Increase_In_Profits_Date = str(First_String_Formatting) + str(Second_String_Formatting) + str(Third_String_Formatting)

Raw_Greatest_Decrease_In_Profits_Date.split("-")
Fourth_String_Formatting = str(Raw_Greatest_Decrease_In_Profits_Date[3]) + str(Raw_Greatest_Decrease_In_Profits_Date[4])
Fifth_String_Formatting = str(Raw_Greatest_Decrease_In_Profits_Date[5])+ str(Raw_Greatest_Decrease_In_Profits_Date[2]) + "20"
Sixth_String_Formatting = str(Raw_Greatest_Decrease_In_Profits_Date[0]) + str(Raw_Greatest_Decrease_In_Profits_Date[1])
Final_Greatest_Decrease_In_Profits_Date = str(Fourth_String_Formatting) + str(Fifth_String_Formatting) + str(Sixth_String_Formatting)

# The following code allowed us to print our final text, including all the previously stored variables, similarly to the analysis
# provided to us on our homework prompt. 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Profit}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Final_Greatest_Increase_In_Profits_Date} (${Greatest_Increase_In_Profits})")
print(f"Greatest Decrease in Profits: {Final_Greatest_Decrease_In_Profits_Date} (${Greatest_Decrease_In_Profits})")

# The following code allowed us to create the Results.txt file for our PyBank folder.
Results = os.path.join('/Users/azpunit/Desktop/python-challenge/PyBank/Analysis/Results.txt')

# The following code allowed us to write exactly the same text that we previously printed in terminal in the Results.txt file of
# our PyBank folder.
with open(Results, 'w') as text:    
    text.write("Financial Analysis" + str("\n"))
    text.write("----------------------------" + str("\n"))
    text.write(f"Total Months: {Total_Months}\n")
    text.write(f"Total: ${Total_Profit}\n")
    text.write(f"Average Change: ${Average_Change}\n")
    text.write(f"Greatest Increase in Profits: {Final_Greatest_Increase_In_Profits_Date} (${Greatest_Increase_In_Profits})\n")
    text.write(f"Greatest Decrease in Profits: {Final_Greatest_Decrease_In_Profits_Date} (${Greatest_Decrease_In_Profits})\n")
