import os
import csv

csv_path=os.path.join("Resources", "budget_data.csv") 

months=0
revenue=0
difference=0
difference_variance = []
month_total = []
increase = 0
highest_month = 0
decrease = 0
lowest_month = 0

with open(csv_path, header = ' ') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader, None)
        row = next(csv_reader)

        profit = int(row[1])
        month_total = month_total + 1
        revenue = revenue + int(row[1])
        increase = int(row[1])
        highest_month = row[0]

for row in csv_reader:
    month_total = month_total + 1
    revenue = revenue + int(row[1])

    variance = int(row[1]) - profit
    variance.append(variance)
    profit = int(row[1])
    month_total.append(row[1])

    if int(row[1]) > increase:
        increase = int(row[1])
        highest_month = row[0]

    if int(row[1]) < increase:
        decrease = int(row[1])
        lowest_month = row[0]

mean_variance =sum(variance)/len(variance)

highest = max(variance)
lowest = min(variance)

print("Months" + str(month_total))
print("Revnue" + str(revenue))
print(mean_variance)
print("highest_month", max(variance))
print("lowest_month", min(variance))
