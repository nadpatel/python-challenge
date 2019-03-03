import csv
import os
import math

polling_original = os.path.dirname('/Users/nadiapatel/Documents/NUCHI201902DATA1/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') #<-- absolute dir the script is in
rel_path = "Resources/budget_data.csv"
abs_file_path = os.path.join(polling_orignal, rel_path)
polling_clean = csv.reader(polling_original, delimiter=',')

f = open(abs_file_path)
print(f.read())

totalvotes = 0
polling_dict = {"Voter_ID":[], "County":[], "Candidate":[]}
Voter_list = polling_dict["Voter_ID"]
County_list = polling_dict["County"]
Candidate_list = polling_dict["Candidate"]
unique_Candidate_list =[]

for row in polling_data:
    Voter_list_length = Voter_list_length + 1
    #get the data appended into lists
    Voter_list.append(row[0])
    County_list.append(row[1])
    Candidate_list.append(row[2])
    #gather the list of unique candidates
  

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

Candidate_list.next() # to skip the header
    for x in Voter_list(Candidate_list): 
        # check if exists in Candidate List or not 
        if x not in unique_Candidate_list: 
            unique_Candidate_list.append(x) 
    # print list 
    for x in unique_Candidate_list: 

unique_Candidate_list_length= len(unique_Candidate_list)

totalvotes = Candidate_list.count(candidate)
if totalvotes > winning_votes:
    winner = candidate
    winning_votes = totalvotes
        
percent_of_votes = totalvotes / Voter_list_length *100
percent_of_votes = round(percent_of_votes,5)

#The winner of the election based on popular vote.

print(" Election Results  ")
print("-------------------")
print(f"Total Votes : {Voter_list_length}")

print("-------------------")
f.write("Election Results ")
f.write("-----------------  ")

f.write("----------------- \r\n \r\n")