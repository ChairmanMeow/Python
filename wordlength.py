import os, fileinput, csv, string, math

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

authors = ("Austen","Byron","Dickens","Dickinson","Emerson","James","Joyce","Keats","London","Melville",
	"Milton","Poe","Shakespeare","Shelly","Swift","Thoreau","Twain","Wilde")

myfile=open('/home/victor/Desktop/wordlength.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(('Average','Variance','BOOKID','Author'))
myfile.close()
writer = csv.writer(open("/home/victor/Desktop/wordlength.csv", 'a'))

for person in authors:
	#Folders are the name of the different books
	folders=get_immediate_subdirectories("/home/victor/Desktop/books/"+person)

	for literature in folders:
		os.chdir("/home/victor/Desktop/books/"+person+"/"+literature)
		names=[]
		for files in os.listdir("."):
		    if files.endswith(".txt"):
		        names.append(files)
		for book in names:
			cwd = os.getcwd()
			myfile = open(book, "r")
			wordcount_sum = 0
			aword=[]
			wordlength_sum = 0
			for line in myfile:
			    words = line.split()
			    # sum up the word counts
			    wordcount_sum += len(words)
			    for word in words:
			        # sum up the word lengths
			        #wordlength_sum += len(word)
			        aword.append(len(word))
			# invoke floating point division for Python versions < 3.0
			wordlength_average = sum(aword)/float(wordcount_sum)
			wordlength_variance = 0
			for word in aword:
				wordlength_variance+=math.pow(word-float(wordlength_average),2)
			wordlength_variance = wordlength_variance/float(wordcount_sum-1)
			writer.writerow([wordlength_average]+[wordlength_variance]+[book.replace(" ", "")]+[person])
		