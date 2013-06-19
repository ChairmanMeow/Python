import json
import os

os.chdir('../pydata-book/ch02')
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
s = open(path).readline()
print s

records = [json.loads(line) for line in open(path)]

print records[0]['tz'] 

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

from collections import defaultdict
def get_counts2(sequence):
	counts = defaultdict(int)
	for x in sequence:
		counts[x] += 1
	return counts

counts = get_counts(time_zones)
counts2 = get_counts2(time_zones)
print counts['America/New_York']
print counts2['America/New_York']
print len(time_zones)

def top_counts(count_dict,n=10):
	value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]
 
print top_counts(counts)
print "\n"

from pandas import DataFrame, Series
import pandas as pd 
frame = DataFrame(records)

print frame['tz'].value_counts()[:10] 
print '\n'
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()[:10]
print tz_counts


import matplotlib.pyplot as plt

tz_counts[:10].plot(kind='barh',rot=0)
plt.show()
