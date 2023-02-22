import os
import csv
input_path = "./Instructions/PyBank/Resources/budget_data.csv"

with open (input_path) as budget_data:

    reader =  csv.reader(budget_data) 
    header = next(reader)
    total = 0
    Count = 0
    count_months = 0

    previous_month_profit_loss = 0
    current_month_profit_loss = 0
    net_profit_loss = 0
    profit_loss_change = 0
    months = []
    profit_loss_changes = []

    for row in reader:
        Profit_Losses = int(row[1])
        Count = Count + 1
        
        total = Profit_Losses + total
        
        count_months += 1
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss
        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)
            previous_months_profit_loss = current_month_profit_loss
            sum_profit_loss = sum(profit_loss_changes)
            average_profit_loss = round(sum_profit_loss/count_months + 1)/86

            highest_change = max(profit_loss_changes)
            lowest_change = min(profit_loss_changes)

            highest_month_index = profit_loss_changes.index(highest_change)
            lowest_month_index = profit_loss_changes.index(lowest_change)

            greatest_increase_month = months[highest_month_index]
            greatest_decrease_month = months[lowest_month_index]


        print(greatest_decrease_month)

        print("Financial Analysis")
        print("------------------------------------")
        print(f"Total months:{Count}")
        print(f"Total: ${total}")
        print(f"Average Change = ${average_profit_loss}")
        print(f"Greatest Increase in Profits: ${greatest_increase_month}")
        print(f"Greatest Decrease in Losses: ${greatest_decrease_month}")

        budget_file = os.path.join("Output","budget_data.txt")
        with open(budget_file, "w") as outfile:

            outfile.write("Financial Analysis\n")
            outfile.write("----------------------------\n")
            outfile.write(f"Total Months {Count}\n")
            outfile.write(f"Total: ${total}\n")
            outfile.write(f"Average Change = ${average_profit_loss}\n")
            outfile.write(f"Greatest Increase in Profits: ${greatest_increase_month}\n")
            outfile.write(f"Greatest Decrease in Losses: ${greatest_decrease_month}\n")


    