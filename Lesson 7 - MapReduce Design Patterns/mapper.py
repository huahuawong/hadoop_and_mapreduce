# get the imports
import sys
import csv
import string

# read csv file
reader = csv.reader(sys.stdin, delimiter='\t')

# parse data to get the id and the words
for line in reader:
	body = line[4]
	id = line[0]
	
	words = body.strip().split()
	for word in words:
        	if 'fantastic' in word.lower():
            		print "{0}\t{1}".format(word.lower(), id)
