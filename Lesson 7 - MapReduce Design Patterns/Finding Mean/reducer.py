# Remember our goal is to find the mean sales for each day
import sys

salesTotal = 0
oldKey = None
count=0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    # if there are still keys (weekday) and it's a different key
    if oldKey and oldKey != thisKey:
        # print the key and its mean, which is sales total divided by the count
        print oldKey, "\t", float(salesTotal/count)
        oldKey = thisKey;
        salesTotal = 0
        count=0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count += 1

if oldKey != None:
	print oldKey, "\t", float(salesTotal/count)
