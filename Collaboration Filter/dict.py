'''
Created on 1 July 2013

@author: Victor Wong

Creates a csv file which is a dictionary of the brand id and brand names.
The dictionary is sosrted alphabetically by brand name.

Python 2.7.2+
'''
import fileinput
import csv

input_file = 'brands_filtered_v2.txt'
writer = csv.writer(open('dict.csv', 'w+'))
d={}

#Add the brand id and name to a dictionary
for each_line in fileinput.input(input_file):
	row = each_line.rstrip('\n').split(';')
	d[row[1]]=row[2]

fileinput.close()

#Sort the dictionary alphabetically
dictsort = sorted(d, key=d.get)
for w in dictsort:
    writer.writerow([w, d[w]])