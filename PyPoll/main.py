# The following code allowed us to locate and create the files that we needed for this assignment, namely, csv and text ones. 
import os
import csv

# The following code allowed us to locate our election_data.csv excel file.
csvpath = os.path.join('/Users/azpunit/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

# The following code allowed us to store the header row into a row and the total number of voters into a variable.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    Total_Of_Voters = len(list(csvreader))

# The following code allowed us to create some lists and elements that helped us store the results that we found into lists and
# variables.
Total_Votes_Per_Candidate = 0
Votes_Format = {}
Candidates_Sample_List = []
Test_Value = [float("inf")]
Voters_List = []

# The following code allowed us to create a list of the candidates who received votes and store the number votes that each
# one received.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    for row in csvreader:
        Total_Votes_Per_Candidate += 1
        Candidate = row[2]
        if Candidate not in Candidates_Sample_List:
            Candidates_Sample_List.append(Candidate)
            Votes_Format[Candidate] = 0
        Votes_Format[Candidate] = Votes_Format[Candidate] + 1

for Candidate, Votes_Number in Votes_Format.items():
    Voters_List.append(Votes_Number)
    if (Test_Value > Voters_List):
        Test_Value = Voters_List
        Winner = str(Candidate)

# The following code allowed us to print our final text similarly to the analysis similarly to the analysis provided to us on
# our homework prompt. 
# We also added the percentages of votes each candidate had by directly plugging the formula before printing everyhting.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Of_Voters}")
print("-------------------------")
for Candidate, Votes_Number in Votes_Format.items():
    Total_Votes_Percentages = str(round(Votes_Number*100/Total_Of_Voters, 3)) +"00%"
    print(f"{Candidate}: {Total_Votes_Percentages} ({Votes_Number})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

# The following code allowed us to create our Results.txt file.
Results = os.path.join('/Users/azpunit/Desktop/python-challenge/PyPoll/Analysis/Results.txt')

# The following code allowed us to write exactly the same text that we previously printed in terminal in the Results.txt file. 
with open(Results, 'w') as text:    
    text.write("Election Results" + str("\n"))
    text.write("-------------------------" + str("\n"))
    text.write(f"Total Votes: {Total_Of_Voters}\n")
    text.write("-------------------------" + str("\n"))
    for Candidate, Votes_Number in Votes_Format.items():
        Total_Votes_Percentages = str(round(Votes_Number*100/Total_Of_Voters, 3)) +"00%"
        text.write(f"{Candidate}: {Total_Votes_Percentages} ({Votes_Number})\n")
    text.write("-------------------------" + str("\n"))
    text.write(f"Winner: {Winner}\n")
    text.write("-------------------------" + str("\n"))
