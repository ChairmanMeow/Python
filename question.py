import os
import fileinput
import csv
from collections import Counter
import re
from string import punctuation

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

#Folders are the name of the different books

punct= ('?',"!",'"',".",',',':',';','{','}','/','\\','|','[',']','_','%','&',"'","(",")","*","+","-",'=',"#","$")

#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


authors = ("Austen","Joyce","Swift","Shakespeare","Twain")
wr = csv.writer(open('/home/victor/Desktop/author.csv', 'wb'))
wr.writerow(('?','BOOKID','Author'))


for person in authors:
	folders=get_immediate_subdirectories("/home/victor/Desktop/books/"+person)

	for literature in folders:
		os.chdir("/home/victor/Desktop/books/"+person+"/"+literature)
		names=[]
		for files in os.listdir("."):
		    if files.endswith(".txt"):
		        names.append(files)
		for book in names:
			cwd = os.getcwd()
			counts = Counter(open(book).read())
 			punctuation_counts = {k:v for k, v in counts.iteritems() if k in punctuation}
 			print [punctuation_counts.get(fieldname,0) for fieldname in punct]
			print book 
			#writer = csv.writer(open("/home/victor/Desktop/author.csv", 'a'))
			#writer.writerow(question+[book.replace(" ", "")]+[person])
