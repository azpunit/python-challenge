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

# The following code allowed us to create some lists that helped us store the results that we found into variables.
List_Of_Voters = []
List_Of_Khan_Voters = []
List_Of_Correy_Voters = []
List_Of_Li_Voters = []
List_Of_O_Tooley_Voters = []

# The following code allowed us to create a list of the candidates who received votes.
List_Of_Candidates = ["Khan", "Correy", "Li", "O'Tooley"]

# The following code allowed to use loops and conditionals in order to store the total number of voters for each candidate
# into variables.
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        List_Of_Voters.append(row[2])

for First_Candidate in List_Of_Voters:
    if First_Candidate == List_Of_Candidates[0]:
        List_Of_Khan_Voters.append(First_Candidate)
Total_Of_Khan_Voters = len(List_Of_Khan_Voters)

for Second_Candidate in List_Of_Voters:
    if Second_Candidate == List_Of_Candidates[1]:
        List_Of_Correy_Voters.append(Second_Candidate)
Total_Of_Correy_Voters = len(List_Of_Correy_Voters)

for Third_Candidate in List_Of_Voters:
    if Third_Candidate == List_Of_Candidates[2]:
        List_Of_Li_Voters.append(Third_Candidate)
Total_Of_Li_Voters = len(List_Of_Li_Voters)

for Fourth_Candidate in List_Of_Voters:
    if Fourth_Candidate == List_Of_Candidates[3]:
        List_Of_O_Tooley_Voters.append(Fourth_Candidate)
Total_Of_O_Tooley_Voters = len(List_Of_O_Tooley_Voters)

# The following code allowed us to store the percentage of voters for each candidate into variables.
Percentage_Of_Khan_Voters = str(round((Total_Of_Khan_Voters/Total_Of_Voters)*100, 1)) +"00%"
Percentage_Of_Correy_Voters = str(round((Total_Of_Correy_Voters/Total_Of_Voters)*100, 1)) +"00%"
Percentage_Of_Li_Voters = str(round((Total_Of_Li_Voters/Total_Of_Voters)*100, 1)) +"00%"
Percentage_Of_O_Tooley_Voters = str(round((Total_Of_O_Tooley_Voters/Total_Of_Voters)*100, 1)) +"00%"

# The following code allowed us to use conditionals to store the winner name in function of its popularity into a variable.
Popularity_Of_Khan = (Total_Of_Khan_Voters/Total_Of_Voters)
Popularity_Of_Correy = (Total_Of_Correy_Voters/Total_Of_Voters)
Popularity_Of_Li = (Total_Of_Li_Voters/Total_Of_Voters)
Popularity_Of_O_Tooley = (Total_Of_O_Tooley_Voters/Total_Of_Voters)
Popularity_Of_All_Of_The_Candidates = [Popularity_Of_Khan, Popularity_Of_Correy, Popularity_Of_Li, Popularity_Of_O_Tooley]
if max(Popularity_Of_All_Of_The_Candidates) == Popularity_Of_Khan:
    Winner = List_Of_Candidates[0]
elif max(Popularity_Of_All_Of_The_Candidates) == Popularity_Of_Correy:
    Winner = List_Of_Candidates[1]
elif max(Popularity_Of_All_Of_The_Candidates) == Popularity_Of_Li:
    Winner = List_Of_Candidates[2]
elif max(Popularity_Of_All_Of_The_Candidates) == Popularity_Of_O_Tooley:
    Winner = List_Of_Candidates[3]

# The following code allowed us to print our final text, including all the previously stored variables, similarly to the analysis
# provided to us on our homework prompt. 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Of_Voters}")
print("-------------------------")
print(f"{List_Of_Candidates[0]}: {Percentage_Of_Khan_Voters} ({Total_Of_Khan_Voters})")
print(f"{List_Of_Candidates[1]}: {Percentage_Of_Correy_Voters} ({Total_Of_Correy_Voters})")
print(f"{List_Of_Candidates[2]}: {Percentage_Of_Li_Voters} ({Total_Of_Li_Voters})")
print(f"{List_Of_Candidates[3]}: {Percentage_Of_O_Tooley_Voters} ({Total_Of_O_Tooley_Voters})")
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
    text.write(f"{List_Of_Candidates[0]}: {Percentage_Of_Khan_Voters} ({Total_Of_Khan_Voters})\n")
    text.write(f"{List_Of_Candidates[1]}: {Percentage_Of_Correy_Voters} ({Total_Of_Correy_Voters})\n")
    text.write(f"{List_Of_Candidates[2]}: {Percentage_Of_Li_Voters} ({Total_Of_Li_Voters})\n")
    text.write(f"{List_Of_Candidates[3]}: {Percentage_Of_O_Tooley_Voters} ({Total_Of_O_Tooley_Voters})\n")
    text.write("-------------------------" + str("\n"))
    text.write(f"Winner: {Winner}\n")
    text.write("-------------------------" + str("\n"))
