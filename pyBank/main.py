import os
import csv
num_row=0
total=0
average=0
i=0
p=1
rr=[]
csv_path=os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
    print(csvreader)
    csv_header=next(csvreader)
    print(csv_header)
    #print(len(list(csvreader)))
    #my_dict={"months":[],"change in profit/loss":[]}

    for row in csvreader:
        num_row +=1
        total += int(row[1])
        #diff=row(i+1)-row(i)
        rr.append(int(row[1]))
       # my_dict["months"].append(row[0])
       # my_dict["profit/loss"].append(row[1])

    #print (f'{my_dict["months"]} and profit{my_dict["profit/loss"]}')


    #average = total/num_row

    #print(num_row)
    #print(total)
    #print(average)
    #print(rr)
    dd_dict={"change":[]}
    l=len(rr)

    c=[]
    for i in range(l-1):
        k=(rr[i])
        d=(rr[i+1])
        #print(k)
        #print(d)
        c.append(d-k) 
         
        
        i=+1 
        dd_dict["change"]=c
    
    print(c)   
    print(f'{dd_dict}')
        
  roster = zip(indexes, employees, department)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerows(roster)  


