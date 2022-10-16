import os
import csv

# Path to collect data from the Resources folder
election_data = csv.DictReader(open('../PyPoll/Resources/election_data.csv'))

# Setting initial variables that will be used later on in the code
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Still not 100% sure on this line but I'm pretty sure it loops through all the rows in the election_data 
for i,row in enumerate(election_data):

    # Counts the total number of votes
    total_votes += 1

    # Counts the votes for each individual candidate by looking for each name
    if row['Candidate'] == "Charles Casper Stockham":
        charles_votes += 1
    elif row['Candidate'] == "Diana DeGette":
        diana_votes += 1
    else:
        raymon_votes += 1

# Calculates the percentage of votes received by each candidate and rounds them to the thousandths place
charles_percent = round(((charles_votes/total_votes) * 100), 3)
diana_percent = round(((diana_votes/total_votes) * 100), 3)
raymon_percent = round(((raymon_votes/total_votes) * 100), 3)

# Conditionals to determine who the winner was and store the name as a variable
if charles_votes > diana_votes and charles_votes > raymon_votes:
    winner = "Charles Casper Stockholm"
elif diana_votes > charles_votes and diana_votes > raymon_votes:
    winner = "Diana DeGette"
elif raymon_votes > charles_votes and raymon_votes > diana_votes:
    winner = "Raymon Anthony Doane"
else:
    winner = "There was an error in calculation"

# Prints the results of my findings in the terminal 
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print(f'Charles Caspter Stockham:   {charles_percent}% ({charles_votes})')
print(f'Diana DeGette: {diana_percent}% {diana_votes})')
print(f'Raymon Anthony Doane: {raymon_percent}% ({raymon_votes})')
print("-------------------------")
print(f'Winner : {winner}')
print("-------------------------")

# Opens path for analysis results
election_analysis = os.path.join('Analysis', 'election_results.txt')

# Outputs all the results to a text file
with open (election_analysis, "w") as file:
    file.write("Election Results")
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')
    file.write(f'Total Votes: {total_votes}')
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')
    file.write(f'Charles Caspter Stockham:   {charles_percent}% ({charles_votes})')
    file.write('\n')
    file.write(f'Diana DeGette: {diana_percent}% {diana_votes})')
    file.write('\n')
    file.write(f'Raymon Anthony Doane: {raymon_percent}% ({raymon_votes})')
    file.write('\n')
    file.write("-------------------------")
    file.write('\n')
    file.write(f'Winner : {winner}')
    file.write('\n')
    file.write("-------------------------")
