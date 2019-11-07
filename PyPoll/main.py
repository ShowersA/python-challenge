import os
import csv

election_data_csv_path = os.path.join("election_data.csv")

Total_votes = 0
candidate_names = []
candidate_votes = []


with open(election_data_csv_path, newline="") as csvfile:
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
    print(str(candidate_names[count]) + ": " + str(percentages[count]) + "% (" + str(candidate_votes[count]) + ")")
print("---------------------------")
print('Winner: '+ str(winner))
print("---------------------------")



output = open("pypoll_results.txt", 'w')

output.write("Election Results\n")
output.write("--------------------------\n")
output.write('Total Votes: ' + str(Total_votes) + "\n")

for count in range(len(candidate_names)):
    output.write(str(candidate_names[count]) + ": " + str(percentages[count]) + "% (" + str(candidate_votes[count]) + ")\n")

output.write("---------------------------\n")
output.write(f"Winner: {winner}\n")
output.write("---------------------------\n")

output.close()  