'''
Created on 1 July 2013

@author: Victor Wong

Creating a simple collaborative filter

Python 2.7.2+
'''
import pandas as pd 
import numpy as np
import time
import fileinput

def loadData(input_file):
	df = pd.read_csv(input_file, sep=';')
	df.columns = ['profile', 'brand','name'] #rename columns
	df = df.ix[:,['profile','brand']] #select first 2 columns
	return df

def loadDict(dictionary):
	d={}
	#Add the brand id and name to a dictionary
	for each_line in fileinput.input(dictionary):
		row = each_line.rstrip('\r\n').split(',',1)
		d[row[0]]=row[1]
	fileinput.close()
	return d

def get_count(values):
	return len(values)

def get_val(values):
	return sum(values)

def findRelatedBrands(df,brand,num):
	dfUsers = df[df['brand'].isin([brand])]['profile']
	dfBrands = df[df['profile'].isin(dfUsers) & (df['brand'] != brand)]

	counts = dfBrands.groupby('brand').brand.agg(get_count)
	topCounts = counts.order(ascending=False)[:num]
	normalizeCounts = topCounts/float(len(dfUsers))
	#Percent of people who favorited this also favorrited these.
	normalizeCounts.name = 'Related Ranking'
	return normalizeCounts

def findWeightedBrands(df,brand,num):
	df['weight'] = 1.0
	dfUsers = df[df['brand'].isin([brand])]['profile']
	dfBrands = df[df['profile'].isin(dfUsers) & (df['brand'] != brand)]

    #Percentage each choice is of overall prefereence
	userCounts = dfBrands.groupby('profile').profile.agg(get_count)
	weights = float(1)/(userCounts) #Weighting function

	#Add the weights to the column
	weightCol = np.repeat(weights.values,userCounts.values.astype(np.int32))
	dfBrands['weight'] = weightCol

	#Find the brands with the highest score
	counts = dfBrands.groupby('brand').weight.agg(get_val)
	topCounts = counts.order(ascending=False)[:num]
	normalizeCounts = topCounts/float(len(userCounts))
	normalizeCounts.name = 'Weighted Ranking'
	return normalizeCounts

def weightFunc(grp):
	grp['weight'] = len(grp)
	#grp['weight'] = (len(grp)-grp.median())/(grp.std())
	#Normalize the weights. Other possibilities could be: 
	#sqrt(1/len(grp))
	#1/(log(len(grp)+1))
	#Explaore other transformation, especially Box-Cox transformations.
	return grp

def addRanks(df):
	df['weight'] = 1.0
	group = df.groupby('brand').weight.agg(get_count)
	groupVals = group.values.astype(float32)
	ranks = pd.DataFrame(groupVals).rank(ascending=False)
	rankedDf = group.sort_index(by='brand',ascending =True)
	rankCol = np.repeat(ranks.values,groupVals.astype(np.int32))
	rankedDf['ranks'] = rankCol
	rankedDf = rankedDf.sort_index(by='profile',ascending =True)
	return rankedDf

def euclidDistance(df):
	#Finish this method using the rank and weights.
	#implement other distance techniques later.
	return df

def findBrandsPopWeight(df,brand,num):
	df['weight'] = 1.0
	df = df.groupby('brand').apply(weightFunc)
	df = modifyWeights(df,brand)
	dfUsers = df[df['brand'].isin([brand])]['profile']
	dfBrands = df[df['profile'].isin(dfUsers) & (df['brand'] != brand)]
	counts = dfBrands.groupby('brand').weight.agg(get_val)
	topCounts = counts.order(ascending=False)[:num]
	topCounts.name = 'Population Modified Weighted Ranking'
	return topCounts

def modifyWeights(df,brand):
	size = df[df['brand']==brand]['weight'].mean()
	a = []
	#Warning! These numbers are arbitrary and need to be fine tuned.
	if size >= 100000:
		a = [.25,.6,.75,.95,5]
	elif size >= 10000:
		a = [.1,.6,.5,.95,2]
	elif size >= 1000:
		a = [.01,.1,.85,.8,3]  
	elif size >= 100:
		a = [.001,.005,.1,.95,.8]
	else:
		a = [.001,.01,.1,.95,5]

	df['weight'][df['weight']>100000] = a[0]
	df['weight'][df['weight']>10000] = a[1]
	df['weight'][df['weight']>1000] = a[2]
	df['weight'][df['weight']>100] = a[3]
	df['weight'][df['weight']>=1] = a[4]   

	return df

def idToName(series,dictionary):
	brands = []
	for id in series.index:
		brands.append(dictionary[str(id)])
	series.index = brands
	return series


###############################################################################
#Beign script
start_time = time.time()
inputf = 'brands_filtered_v2.txt'
dictf = 'dict.csv'           

#Load the data
df = loadData(inputf)
d = loadDict(dictf)

#Find top 10 matches for brand 51, BCBG
brand1 = 51 #BCBG
brand2 = 2685 #Tag
relatedNum = 10
result1 = findBrandsPopWeight(df, brand1, relatedNum)
result2 = findBrandsPopWeight(df, brand2, relatedNum)

#Brand 1
print idToName(result1, d) 
print '\n'
#Brand 2
print idToName(result2, d) 
print '\n'
print time.time() - start_time, "seconds"

'''
Output

Victoria's Secret        18077.4
Prada                    17821.8
Steve Madden             16746.6
Juicy Couture            16582.8
Forever 21               15910.2
Diane von Furstenberg    14362.8
MICHAEL Michael Kors     14005.8
GUESS                    13549.8
Marc Jacobs              13153.8
Tory Burch               12945.0
Name: Population Modified Weighted Ranking


Wet Seal       1377.85
Aeropostale    1192.55
Delia's         916.30
Urban Decay     847.45
Arden B         824.50
Alloy           670.65
Halston         623.90
Roxy            620.50
philosophy      598.40
Maybelline      594.15
Name: Population Modified Weighted Ranking


49.1163311005 seconds

'''