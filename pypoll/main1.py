import os
import csv
#defining variables
total_votes=0
cand_name=[]
cand_vote=[]
unique_cand=[]
# Defining path to read CSV file.
csv_path=os.path.join("Resources", "election_data.csv")

# Reading the csv file 
with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)


# Loop to get Total Votes and Create Two list 
# 1)Cand_name(has the list of all occurances of candidate)
# 2)cand_vote(total voter ID lis)    
    for row in csvreader:
        total_votes+=1
        cand_name.append(row[2])
        cand_vote.append(row[0])


#getting Unique candidate
candidate_list = []
for candidate in set(cand_name):
    candidate_list.append(candidate)


#printing Total votes
print(f'     The Elections Results          ')
print(f'-----------------------------------------------------------')
print(f'Total Votes are  {total_votes}')
print(f'-----------------------------------------------------------')


# loop to get the total number of votes, percentage for each candidate
l=len(candidate_list)
percent_value=[]
count=0
count_tot_vote=[]
tl=len(cand_name)
for y in range(l):
    count=0
    for x in range(tl):
        if cand_name[x]==candidate_list[y]:
                count+=1
    count_tot_vote.append(count)
    percent_value.append((count/total_votes)*100)
    print(f'Mr. {candidate_list[y]} got vote percentage: {percent_value[y]} with a total vote_count: {count_tot_vote[y]} ')

# finally, finding the winner and printing it
Max_vote= max(count_tot_vote)
winner=candidate_list[(count_tot_vote.index(Max_vote))]
print(f'-----------------------------------------------------------')
print(f'And the Winner is....DrumRoll.......... Mr.{winner} !!!!!!!!')
print(f'-----------------------------------------------------------')

csv_outpath=os.path.join("analysis",output.txt)
with open(csv_output,)

