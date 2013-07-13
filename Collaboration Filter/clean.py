'''
Created on 1 July 2013

@author: Victor Wong

Modified data cleaning script. Converts to csv seperated by semicolons
Also checks if rows are all in the same format.

Python 2.7.2+
'''
import fileinput

input_file = 'brands_filtered.txt'
outpath = 'brands_filtered_v2.txt'

with open(outpath, 'w+') as output:
    for each_line in fileinput.input(input_file):
        output.write(each_line.replace('\t',';',2))

		#Checks if rows are all in the same format.
        splitline = each_line.replace('\t',';',2).split(';')
        if len(splitline) != 3:
	        first_bad_line = splitline
	        print "First bad row:", i
	        for j, col in enumerate(first_bad_line):
	            print j, col
	        break

fileinput.close()

print 'ALL GOOD'