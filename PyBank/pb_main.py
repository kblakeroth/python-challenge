import os
import csv

#join and describe path
csv_file_path = os.path.join("budget_data.csv")

# initialize variables
total_months  =  0       # total number or months
total_revenue = 0        # total profit/losses
prev_revenue  = 0       # previous profit/losses
profit_delta  = 0
revenue_delta_list = [] # list of differences between consecutive rows
greatest_increase_profits = ['', 0]            # start with smallest number that is possible
greatest_decrease_losses = ['', 9999999999999] # start with huge number that is bigger than possible
#-----------------------------------------------------------

with open(csv_file_path, newline="") as csv_file: 
    reader = csv.DictReader(csv_file)
    for row in reader:       
        total_months += 1 # count up total number months       
        total_revenue += int(row['Profit/Losses']) # calculate total profit/losses
        # used to calulate average change in profit/losses between months
        if total_months == 1: # there is no delta for first row because it has no previous row to subtract
            prev_revenue = int(row["Profit/Losses"])
        else:
            profit_delta = int(row["Profit/Losses"]) - prev_revenue
            prev_revenue = int(row["Profit/Losses"])
            revenue_delta_list = revenue_delta_list + [profit_delta]
       
        # find greatest increase in profit (date and amount)
        if profit_delta > greatest_increase_profits[1]:
            greatest_increase_profits[1] = profit_delta
            greatest_increase_profits[0] = row['Date']
           
        # find greatest decrease in losses (date and amount)
        if profit_delta < greatest_decrease_losses[1]:
            greatest_decrease_losses[1] = profit_delta
            greatest_decrease_losses[0] = row['Date']

average_change_revenue = sum(revenue_delta_list)/len(revenue_delta_list) # calulate average change in profit/losses

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Profit/Losses: $" + str(total_revenue))
print(f"Average Change in Profits/Losses: ${average_change_revenue:.2f}")
print("Greatest Increase in Profits: " + str(greatest_increase_profits[0]) + " ($" + str(greatest_increase_profits[1]) + ")")
print("Greatest Decrease in Losses: " + str(greatest_decrease_losses[0]) + " ($" + str(greatest_decrease_losses[1]) + ")")

#describe output file where results will be located
output_file = "main_results.txt"

with open(output_file, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write("Total Months: %d\n" % total_months)
    outfile.write("Total Profits/Losses: $%d\n" % total_revenue)
    outfile.write(f"Average Change in Profits/Losses: ${average_change_revenue:.2f}\n")
    outfile.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase_profits[0], greatest_increase_profits[1]))
    outfile.write("Greatest Decrease in Losses: %s ($%s)\n" % (greatest_decrease_losses[0], greatest_decrease_losses[1]))