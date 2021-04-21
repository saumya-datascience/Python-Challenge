import os
import csv
#defining variables
total_votes=0
poll_result={}
cand_name=[]
unique_cand=[]
csv_path=os.path.join("Resources", "election_data.csv")
#reading the csv file 
with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    print(csvreader)
    csv_header=next(csvreader)
    print(csv_header)
    
    for row in csvreader:
        total_votes+=1
        cand_name.append(row[2])
        
#print (cand_name)

list_1 = []
for candidate in set(cand_name):
    list_1.append(candidate)
print(list_1)
#for i in cand_name:
 #   if i not in cand_name:
  #   unique_cand.append(i)
#print(unique_cand) 

#print(total_votes)



