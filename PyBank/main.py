import os
import csv

# Path to collect data from the Resources folder
budget_data =  csv.DictReader(open('../PyBank/Resources/budget_data.csv'))

# Defining variables that will be needed for code
months = 0
total = 0
total_change =0
greatest_increase = 0
greatest_decrease = 0

# Still not 100% sure on this line but I'm pretty sure it loops through all the rows in the budget_data 
for i,row in enumerate(budget_data):

    months += 1 #Counts up all the rows to tell me how many total months there are
    profit = int(row['Profit/Losses']) #Reads all the values from the profit/losses row as integers
    total += profit #Adds all the profits and losses from the column to get the total profit

    # Creates the variable last_profit so we can later find the change in every month
    if i == 0:
        last_profit = profit

    monthly_change = profit - last_profit # Calculates the change in profit from each month
    total_change += monthly_change # Adds all the values for monthly change to calculate the total amount of change from the first to last month
    last_profit = profit # Resets profit so we can see the change in the following months

    # Finds the largest increase from month to month and saves that value along with the matching date
    if monthly_change > greatest_increase:
        greatest_increase = monthly_change
        increase_date = row['Date']

    # Finds the largest decrease from month to month and saves that value along with the matching date
    if monthly_change < greatest_decrease:
        greatest_decrease = monthly_change
        decrease_date = row['Date']
    
# Calculate the average change and round it to the hundredths place    
average_change = round((total_change)/(months-1), 2)

# Prints the results of my findings in the terminal 
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase_date} ({greatest_increase})')
print(f'Greatest Decrease in Profits: {decrease_date} ({greatest_decrease})')

# Opens path for analysis results
budget_analysis = os.path.join('Analysis', 'budget_results.txt')

# Outputs all the results to a text file
with open (budget_analysis, "w") as file:
    file.write("Financial Analysis")
    file.write('\n')
    file.write("----------------------------")
    file.write('\n')
    file.write(f'Total Months: {months}')
    file.write('\n')
    file.write(f'Total: ${total}')
    file.write('\n')
    file.write(f'Average Change: ${average_change}')
    file.write('\n')
    file.write(f'Greatest Increase in Profits: {increase_date} ({greatest_increase})')
    file.write('\n')
    file.write(f'Greatest Decrease in Profits: {decrease_date} ({greatest_decrease})')