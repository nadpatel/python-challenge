import os
import csv


script_dir = os.path.dirname('/Users/nadiapatel/Documents/NUCHI201902DATA1/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') #<-- absolute dir the script is in
rel_path = "Resources/budget_data.csv"
abs_file_path = os.path.join(script_dir, rel_path)

#budget_data = os.path.join('Resources', 'budget_data.csv')
f = open(abs_file_path)
print(f.read())


csvreader = csv.reader(budget_data, delimiter=',')
next(csvreader)  
row_count = 0 
total_profit = 0 
budget_dict = {"Month": [], "Profit/Loss" : []}
PL_List = budget_dict["Profit/Loss"]
PL_List_length = len(PL_List)  

#The net total amount of "Profit/Losses" over the entire period 
for row in csvreader:  
    row_count= row_count+ 1
    total_profit += int(row[2])
    budget_dict["Month"].append(row[1])
    budget_dict["Profit/Loss"].append(row[1])

print (total_profit)
    
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period.
# The greatest decrease in losses (date and amount) over the entire period 
 
for i in range(1,PL_List_Length):
        if i == 0:
            next
        elif i == PL_List_Length-1:
            nxt = 0
            change = int(PL_List[i]) - int(PL_List[i-1])
            rev_change.append(change)   
        else: 
            nxt = PL_List[i+1] 
            change = int(PL_List[i]) - int(PL_List[i-1])
            rev_change.append(int(change))

avg_rev_change = sum((int(PL_List))/PL_List_Length

max_rev_change = max(rev_change)

min_rev_change = min(rev_change)

max_rev_change_date = str(date[rev_change.index(max(rev_change))])
min_rev_change_date = str(date[rev_change.index(min(rev_change))])

print("Financial Analysis")
print("------------------------")
print(f"Total Months: ", PL_List_Length)
print(f"Average Revenue: $", round(avg_rev_change))
print(f"Greatest Increase in Profits: ", max_rev_change_date,"($", max_rev_change,")")
print(f"Greatest Decrease in Profits: ", min_rev_change_date,"($", min_rev_change,")")
