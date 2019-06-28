import os
import csv

# Show the path
budget_data = "/Users/muralipremkumar/Desktop/RICE_DATA/RICEHOU201906DATA1/HW/03-Python/Instructions/PyBank/Resources/budget_data.csv"

 
# Set Variables
Total_months = 0
Profit_loss = 0
Current_row = 0
Previous_row = 0
DiffSum = 0
Previous_month = 0
Increase = 0
Max = 0
Max_month = ""
Decrease = 0
Min = 0
Min_month = ""


# Open CSV file and read 
with open(budget_data,'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        Total_months = Total_months + 1
        Profit_loss = Profit_loss + int(row[1])
        if Total_months >= 2:
            Previous_row = Current_row
            Current_row = int(row[1])
            DiffSum = DiffSum + (Current_row - Previous_row)
        else:
            Current_row = int(row[1])

        if Total_months >=2:
            Previous_max = Max
            Previous_max_month = Max_month
            Current_row = int(row[1])
            Max_month = row[0]
            if Current_row < Previous_max:
                Max_month = Previous_max_month
            else:
                Increase = Current_row - Previous_row
                Max = Current_row
            Previous_row = Current_row

        if Total_months >=2:
            Previous_min = Min
            Previous_min_month = Min_month
            Current_min_row = int(row[1])
            Min_month = row[0]
            if Current_min_row > Previous_min:
                Min_month = Previous_min_month
            else:
                Decrease = Current_min_row - Previous_min_row
                print(Current_min_row, Previous_min_row)
                Min = Current_min_row
            Previous_min_row = Current_min_row




    print("Total number of months included in the dataset = ", Total_months)
    print("The net total amount of Profit/losses over the entire period = ", "$", Profit_loss)
    print("Average of changes over the entire period = ", "$", DiffSum/(Total_months-1))
    print("The greatest increase in profit over the entire period was in ", Max_month,"with $", Max, Increase)
    print("The greatest decrease in profit over the entire period was in ", Min_month,"with $", Min, Decrease)
    
  

  
    
    


