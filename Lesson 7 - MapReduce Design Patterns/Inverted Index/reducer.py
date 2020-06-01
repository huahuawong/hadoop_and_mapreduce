# the imports
import sys

# intialize count and empty list to display
count = 0
list = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	# some data might not have keys and values, so if the length is not equals to 2, we skip it
  if len(data_mapped) != 2:
		continue
	
  # split the data to their respective keys and values
	thisKey, thisValue = data_mapped
	
	if 'fantastic' in thisKey:
    count += 1

		

list = sorted(list)
print "{0}\t{1}".format(count, list)
