import os
import csv

# Show the path
election_data = "/Users/muralipremkumar/Desktop/RICE_DATA/RICEHOU201906DATA1/HW/03-Python/Instructions/PyPoll/Resources/election_data.csv"

# Variables
Total_votes = 0
Candidate = []
#Counter = []
Counter1 = 0
Counter2 = 0
Counter3 = 0
Counter4 = 0
# Open csv file and read
with open(election_data, 'r', newline='')as csvfile:

    #cvsreader specifies delimiter and variables that hold content
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header. Skip if there is no header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    for row in csvreader:
        Total_votes = Total_votes + 1
        if row[2] not in Candidate:
            Candidate.append(row[2])
        
    Candidate = list(dict.fromkeys(Candidate))
    for name in Candidate:
       print(name)
    
    print(Candidate[0])
    print(Candidate[1])
    print(Candidate[2])
    print(Candidate[3])

with open(election_data, 'r', newline='')as csvfile:

    csvreader1 = csv.reader(csvfile, delimiter=',')

    csv_header1 = next(csvreader1)
    print(f"CSV Header Again: {csv_header1}")
    for row1 in csvreader1:
        #print(row1)
        if row1[2] == Candidate[0]:
            Counter1 += 1
        elif row1[2] == Candidate[1]:
            Counter2 += 1
        elif row1[2] == Candidate[2]:
            Counter3 += 1
        elif row1[2] == Candidate[3]:
            Counter4 += 1
    print("----------------------------------------------------------------")
    print("Election Results")
    print("----------------------------------------------------------------")
    print("Total votes:",Total_votes)
    print("----------------------------------------------------------------")
    print(Candidate[0], "=", (Counter1/Total_votes)*100,"%,",Counter1)
    print(Candidate[1], "=", (Counter2/Total_votes)*100,"%,", Counter2)
    print(Candidate[2], "=", (Counter3/Total_votes)*100,"%,", Counter3)
    print(Candidate[3], "=", (Counter4/Total_votes)*100,"%,", Counter4)
