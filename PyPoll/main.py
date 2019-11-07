import os
import csv

election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")

Total_votes = 0
candidate_names = []
#Winner = ""
#winner_count = 0
candidate_votes = []
#Tracker = {}

with open('election_data.csv', newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    Header = next(csv_reader)
    for row in csv_reader:
        Total_votes = Total_votes + 1
        candidate_name = row[2]
        if candidate_name in candidate_names:
            candidate_num = candidate_names.index(candidate_name)
            candidate_votes[candidate_num] = candidate_votes[candidate_num] + 1
        else:
            candidate_names.append(candidate_name)
            candidate_votes.append(1)

percentages = []
highest_vote = candidate_votes[0]
highest_vote_index = 0

for count in range(len(candidate_names)):
    candidate_percentage = round(candidate_votes[count]/Total_votes*100,3)
    percentages.append(candidate_percentage)
    if candidate_votes[count] > highest_vote:
        highest_vote = candidate_votes[count]
        print(highest_vote)
        highest_vote_index = count
winner = candidate_names[highest_vote_index]
print('Election Results')
print('-------------------')
print('Total Votes: ' + str(Total_votes))
print('-------------------')
for count in range(len(candidate_names)):
    print(f"{candidate_names[count]}: {percentages[count]}% ({candidate_votes[count]})")
print("---------------------------")
print('Winner: '+ str(winner))
print("---------------------------")

#print("Election Results")
#print("--------------------------")
#print(f"Total Votes: {num_votes}")

#for count in range(len(candidates)):

 #   print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")

#print("---------------------------")
#print(f"Winner: {winner}")
#print("---------------------------")



write_file = f"pypoll_results.txt"
filewriter = open(write_file, mode = 'w')


filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write('Total Votes: ' + str(Total_votes))

for count in range(len(candidate_names)):
    filewriter.write(f"{candidate_names[count]}: {percentages[count]}% ({candidate_votes[count]})\n")

filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")



#close file
filewriter.close()

    