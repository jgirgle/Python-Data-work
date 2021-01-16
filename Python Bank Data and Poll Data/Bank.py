import pathlib
import csv

# Path to collect data from the folder
budget_csv = pathlib.Path('Resources/budget_data.csv')
pathout = pathlib.Path("Resources/Bank Analysis")
# Variable Track
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = [",", 0]
greatest_decrease = ["", 99999999999999999]

revenue_changes = []

# Read CSV File
with open(budget_csv) as revenue_data:
    reader = csv.DictReader(revenue_data)
    jan_start = next(reader)
    total_months = total_months + 1
    prev_revenue =int(jan_start["Profit/Losses"])
    total_revenue = total_revenue + int(jan_start["Profit/Losses"]) 
    for row in reader:

        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        #print(row)

        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        # print(row['Date'])
        # print(revenue_change)

        prev_revenue = int(row["Profit/Losses"])
        # print(prev_revenue)

        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        revenue_changes.append(revenue_change)

    revenue_average = round(sum(revenue_changes) / len(revenue_changes), 2)
    


    print()
    print()
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Change: ${revenue_average}")
    print(f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open(pathout, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {total_months}")
    txt_file.write("\n")
    txt_file.write(f"Total Revenue: ${total_revenue}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: ${revenue_average}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})")