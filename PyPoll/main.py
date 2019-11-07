import os
import csv

election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")

Total_votes = 0
Candidate_names = []
Winner = ""
winner_count = 0
Tracker = {}

with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    Header = next(csv_reader)
    for row in csv_reader:
        Total_votes = Total_votes + 1
        Candidates = row[2]
        #if candidate
#Total Votes
print('Total Votes: ' + str(Total_votes))
#Total Votes per Candidate
#Percentage of Votes per Candidate
#Winner



    