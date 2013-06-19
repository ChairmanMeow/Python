#Stat 154 Get passages of texts 
import os
import fileinput

authors = ("Austen","Byron","Dickens","Dickinson","Emerson","James","Joyce","Keats","London","Melville",
	"Milton","Poe","Shakespeare","Shelly","Swift","Thoreau","Twain","Wilde")

for person in authors:
	os.chdir("/home/victor/Desktop/books/"+person)

	names=[]

	for files in os.listdir("."):
	    if files.endswith(".txt"):
	        names.append(files)
	for book in names:

		directory = os.path.splitext(book)[0]

		if not os.path.exists(directory):
		    os.makedirs(directory)

		i = 0
		fout = open(directory+"/"+directory+str(i)+".txt","wb+")
		for line in fileinput.FileInput(book):
		  fout.write(line)
		  i+=1
		  if i%1000 == 0:
		    fout.close()
		    fout = open(directory+"/"+directory+"%d.txt"%(i/1000),"wb+")

		fout.close()  
