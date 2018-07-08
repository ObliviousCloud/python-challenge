import os 
import csv


file = os.path.join("Resources","budget_data.csv")


months = []
revenue = []
total_revenue_change = []
prev_net = 0
total_revenue = 0
greatest_change = 0
lowest_change = 0


with open(file, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)


	for row in csvreader:
		months.append(row[0])
		revenue.append(int(row[1]))


for row in range(len(revenue)):
	total_revenue = total_revenue + revenue[row]
	prev_net = revenue[row] - prev_net
	total_revenue_change.append(prev_net)
	prev_net = revenue[row]


del(total_revenue_change[0])


for i in range(len(total_revenue_change)):
	if total_revenue_change[i] >= greatest_change:
		greatest_change = total_revenue_change[i]
		greatest_month = months[i + 1]
	elif total_revenue_change[i] <= lowest_change:
		lowest_change = total_revenue_change[i]
		lowest_month = months[i + 1]


with open("pypoll.txt", 'w') as writeFile:
	writeFile.write("Financial Analysis")
	writeFile.write("\n------------------\n")
	writeFile.write("Total Months: " + str(len(months)) + '\n')
	writeFile.write("Total: $" + str(total_revenue) + '\n')
	writeFile.write("Average Change: $" + str(round(sum(total_revenue_change) / int(len(total_revenue_change)),2)) + '\n')
	writeFile.write("Greatest Increase in Profits: " + str(greatest_month) + " ($" + str(round(greatest_change, 2)) + ")" +'\n')
	writeFile.write("Lowest Decrease in Profits: " + str(lowest_month) + " ($" + str(round(lowest_change, 2)) + ")" +'\n')


#open the Analysis file and print to terminal
with open("pypoll.txt", 'r', newline="") as readFile:
	print(readFile.read())