import os
import csv


csv_path=os.path.join("Resources", "budget_data.csv")

#reading the csv file and excluding the header
with open(csv_path) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=",")
   # print(csvreader)
    csv_header=next(csvreader)

    num_row=0
    total=0
    profitloss_list=[]
    name_list=[]
   #reading the file and making two lists, 1)for months and 2) for profit/loss
    for row in csvreader:
        num_row +=1
        total += int(row[1])
        profitloss_list.append(int(row[1]))
        name_list.append(row[0])
#calculating the Total   
    l=len(profitloss_list)
    Average=total/l
    
#calculating the total change through time
    i=0
    c=[]
    total_change=0
    for i in range(l-1):
        k=(profitloss_list[i])
        d=(profitloss_list[i+1])
        c.append(d-k) 
        total_change=c[i]+total_change
         
    average_change=total_change/(l-1)
 # excluding the first row   
    change_name=name_list[1:]
#getting the max and min values for the profit and loss and corresponding months
#max = max(roster.keys(), key=(lambda k: roster[k]))
#min = min(roster.keys(), key=(lambda k: roster[k]))
max_value=max(c)
min_value=min(c)



#getting index value for the profit or loss changes with respect to months list
max_month=change_name[(c.index(max_value))]
min_month=change_name[(c.index(min_value))]



# Generate Paragraph Analysis Output
output = (
    f"\nFinancial Analysis\n"
    f"-----------------------------------------------------------\n"
    f"Total Months {l}\n"
    f"-----------------------------------------------------------\n"
    f"Total  ${total}\n"
    f"Average Change ${average_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_value})\n"
    f"Greatest decrease in Profits: {min_month} (${min_value})\n")

# Print all of the results (to terminal)
print(output)

# Save the results to analysis text file
output_path=os.path.join("analysis","output.txt")
with open(output_path, "a") as txt_file:
    txt_file.write(output)



