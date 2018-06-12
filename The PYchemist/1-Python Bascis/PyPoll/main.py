# Goal here is to read a file of votes and calculate who won.
# Read through the file once and collect the candidates and counts
# of those respective candidates.

#importing the libraries needed
import os
import csv

path = os.path.join('election_data_2.csv')

# creating two arrays, that will hold the candidates in the vote
# and their respective counts. Setting them as empty to begin
candidates = []
count = []

# Using DictReader to locate and read the candidate column
with open(path, newline='') as lookup:
    reader = csv.DictReader(lookup)
    
    # for loop will commence the reading line by line and extracting of the information
    for x in reader:
        # Setting the variable cand to the candidate of the line being read
        cand = x["Candidate"]

        # super usefull if statement that adds a candidate to a list
        # of candidates  if that person does not exist in the list.
        # It also adds a count of zero at the index of the candidate
        # So the list grows as more unique candidates are counted
        if cand not in candidates:
            candidates.append(cand)
            count.append(0)

        # adds 1 to the counter at the index of the candidate    
        count[candidates.index(cand)] +=1

# The following calculates the sum and percentage and winner and prints them out        
total = sum(count)
winner = count.index(max(count))
print("\nElection Results \n------------------------")
print(f"Total Votes: {total} \n------------------------")
# doing a for loop because we do not know the number of candidadates
# so the length of candidates[] can do that 
for i in range(len(candidates)):
    print(f"{candidates[i]}: {'{:.1%}'.format(float(count[i]/total))}  ({count[i]})")
print(f"------------------------\nWinner is: {candidates[winner]}\n")

# Writing the files in the same format as the printed version
filename='output_data2.txt'
outpath = os.path.join(filename)
with open(outpath, "w") as datafile:
    
    datafile.write("Election Results \n------------------------\n")
    datafile.write(f"Total Votes: {total} \n------------------------")
    for i in range(len(candidates)):
        datafile.write(f"\n{candidates[i]}: {'{:.1%}'.format(float(count[i]/total))}  ({count[i]})")
    datafile.write(f"\n------------------------\nWinner is: {candidates[winner]}\n")