import os
import csv

#Set file path
vote_path = os.path.join("Resources","election_data.csv")

#Set variable
total_votes = []
candidates_dup = []
candidates = []
one_votes = 0
two_votes = 0
three_votes = 0
four_votes = 0
#Getting total votes
with open(vote_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes.append(row[0])
        candidates_dup.append(row[2])
        
    for i in range(len(total_votes)):
        if candidates_dup[i]  not in candidates:
            candidates.append(candidates_dup[i])
# Run this to see how many candidates we have
#print(f'{candidates}')
#['Khan', 'Correy', 'Li', "O'Tooley"]
    
    #calculate votes for each candidates
    for i in range(len(total_votes)):
        if candidates_dup[i] == candidates[0]:
            one_votes = one_votes + 1
        if candidates_dup[i] == candidates[1]:
            two_votes = two_votes + 1
        if candidates_dup[i] == candidates[2]:
            three_votes = three_votes + 1
        if candidates_dup[i] == candidates[3]:
            four_votes = four_votes + 1
votes = [one_votes,two_votes,three_votes,four_votes]
#get winner
max_vote = max(votes)
winner = candidates[votes.index(max_vote)]

#get percentage for each candidates
one_percentage = round((one_votes / len(total_votes))*100,2)
two_percentage = round((two_votes / len(total_votes))*100,2)
three_percentage = round((three_votes / len(total_votes))*100,2)
four_percentage = round((four_votes / len(total_votes))*100,2)

#print result

print("Election Results")
print("-----------------------")
print(f'Total Votes: {len(total_votes)}')
print("-----------------------")
print(f'{candidates[0]}: {one_percentage}00% ({one_votes})')
print(f'{candidates[1]}: {two_percentage}00% ({two_votes})')
print(f'{candidates[2]}: {three_percentage}00% ({three_votes})')
print(f'{candidates[3]}: {four_percentage}00% ({four_votes})')
print("-----------------------")
print(f'Winner: {winner}')
print("-----------------------")

#output text file
output_path = os.path.join("result")

with open(output_path,'w') as textfile:
    
    textfile.write("Election Results\n")
    textfile.write("-----------------------\n")
    textfile.write(f'Total Votes: {len(total_votes)}\n')
    textfile.write("-----------------------\n")
    textfile.write(f'{candidates[0]}: {one_percentage}00% ({one_votes})\n')
    textfile.write(f'{candidates[1]}: {two_percentage}00% ({two_votes})\n')
    textfile.write(f'{candidates[2]}: {three_percentage}00% ({three_votes})\n')
    textfile.write(f'{candidates[3]}: {four_percentage}00% ({four_votes})\n')
    textfile.write("-----------------------\n")
    textfile.write(f'Winner: {winner}\n')
    textfile.write("-----------------------\n")
