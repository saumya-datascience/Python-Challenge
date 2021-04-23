import os
import csv
num_row=0
total=0
average=0
i=0
p=1
rr=[]
mg=[]
roster={}
total_change=0
csv_path=os.path.join("Resources", "budget_data.csv")
#reading the csv file 
with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    print(csvreader)
    csv_header=next(csvreader)
    print(csv_header)
   #reading the file and making two lists, 1)for months and 2) for profit/loss
    for row in csvreader:
        num_row +=1
        total += int(row[1])
        rr.append(int(row[1]))
        mg.append(row[0])
      
    l=len(rr)
    print(total)
    Average=total/l
    print(l)

    c=[]
    for i in range(l-1):
        k=(rr[i])
        d=(rr[i+1])
        c.append(d-k) 
        total_change=rr[i]+total_change
        i=+1 
    
    average_change=total_change/(l-1)
    print(average_change)
    print(c)   
change_name=mg[1:]
#zipping the Lists of months and changes in a dictionary
#roster = dict(zip(mg, c))
#print(roster)
#getting the max and min values for the profit and loss and corresponding months
#max = max(roster.keys(), key=(lambda k: roster[k]))
#min = min(roster.keys(), key=(lambda k: roster[k]))
max_value=max(c)
min_value=min(c)
print(max_value)
print(min_value)
print(change_name)

#getting index value for the profit or loss changes with respect to months list
max_month=change_name[(c.index(max_value))]
min_month=change_name[(c.index(min_value))]
print(max_month)
print(min_month)




# save the output file path
output_file = os.path.join("analysis","output.txt")


# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow("Financial Analysis")             
    writer.writerow("Total Months:")
    writer.writerow("Total:")
    writer.writerow("Average Change:")
    writer.writerow("Greatest Increase in Profits:")
    writer.writerow("Greatest Decrease in profits:")

   

