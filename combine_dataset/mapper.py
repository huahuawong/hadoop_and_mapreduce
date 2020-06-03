import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:

        # YOUR CODE HERE
        if len(line) == 5:
            writer.writerow([line[0]] + ['A'] + line[1:])
        elif len(line) == 19:
    	    writer.writerow([line[3]] + ['B'] + line[:3] + line[5:10])

if __name__=='__main__':
    mapper()   
