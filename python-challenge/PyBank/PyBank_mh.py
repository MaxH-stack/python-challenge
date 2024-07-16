# Import Modules
import os
import csv

# File path to csv
path = os.path.join('..', 'Resources', 'budget_data.csv')
#print(path)

# Read the csv
with open(path) as budgetData:
    csvreader = csv.reader(budgetData, delimiter=',')
    #print(csvreader)

    # Data contains header so it is skipped
    next(csvreader)

# Count total months (rows skipping header)
# Find sum of profit/loss
    Months = 0
    Total = 0
    running_tot = []
    

    for rows in csvreader:
        # Add month to counter
        Months += 1
        
        # Add profit/loss to total
        a = int(rows[1])
        Total = Total + a

        


            
               
        
        
    print(f'Financial Analysis')
    print(f'--------------------------------')
    print(f'Total Months: {Months}')
    print(f'Total: {Total}')
    print(f'Average Change: ')
    print(f'Greatest Increase in Profits: ')
    print(f'Greatest Decrease in Profits: ')
    

    # Average
    #AverageChange = Total / Months
    #print(f'Average Change: {running_tot}')

    
    
