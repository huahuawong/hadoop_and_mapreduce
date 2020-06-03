import sys
from datetime import datetime

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
  # now we have data with length of 2, consisting of weekday, and the cost
	print "{0}\t{1}".format(weekday, cost)