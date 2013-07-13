'''
Created on 1 July 2013

@author: Victor Wong

Checking that all rows are in the same format.

'''

inpath = 'brands_filtered_v2.txt'
 
inf = open(inpath, 'r')
for i, line in enumerate(inf):
    splitline = line.split(';')
    if len(splitline) != 3:
        first_bad_line = splitline
        print "First bad row:", i
        for j, col in enumerate(first_bad_line):
            print j, col
        break

print 'ALL GOOD'
inf.close()