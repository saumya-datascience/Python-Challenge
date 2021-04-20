import os
import csv
num_row=0
total=0
average=0
i=0
rr=[]
csv_path=os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    print(csvreader)
    csv_header=next(csvreader)
    print(csv_header)
    #print(len(list(csvreader)))

    for row in csvreader:
        num_row +=1
        total += int(row[1])
        #diff=row(i+1)-row(i)
        rr.append(int(row[1]))
    average = total/num_row
    
    print(num_row)
    print(total)
    print(average)
    print(rr)


