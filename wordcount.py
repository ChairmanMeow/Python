import os, fileinput, csv, re, string
from collections import Counter
from string import punctuation

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]


text = ("a","all","also","an", "and", "any","are","as","at","be", "been" ,"but","by","can","do",
		"down","even" ,"every","for", "from" , "had" ,"has", "have", "her", "his", "if", 
		"in", "into", "is","it", "its", "may", "more", "must", "my", "no", "not", "now", 
		"of", "on","one","only","or", "our", "should", "so","some", "such", "than", "that", 
		"the", "their", "then" ,"there", "things","this", "to", "up", "upon","was", "were",
		"what", "when" , "which" , "who" , "will" , "with" , "would" , "your")

#punct= ('!','"','#',"$",'%','&',"'",'(',')','*','plus',',','minus','period','/',':','semicolon','<',"=",">","?","@","[","backslash",']',"^","_",
#		"`",'{',"|","}","~")
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
punct= ('exlamation','quote','pound','money','percent','amp','apost','rparens',	'lparens','asterik','plus','comma','minus',
	'period','slash','colon','semicolon','rcarrot','equal','lcarrot','question','atsign','rbracket','backslash','rbracket',
	'carrot','underscore','grave','rcurly','bar','lcurly','tilda')

authors = ("Austen","Byron","Dickens","Dickinson","Emerson","James","Joyce","Keats","London","Melville",
	"Milton","Poe","Shakespeare","Shelly","Swift","Thoreau","Twain","Wilde")

myfile=open('/home/victor/Desktop/author.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(text+punct+('BOOKID','Author'))
myfile.close()
writer = csv.writer(open("/home/victor/Desktop/author.csv", 'a'))

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
			punct_counter = Counter(open(book).read())
 			punctuation_counts = {k:v for k, v in punct_counter.iteritems() if k in punctuation}
			counts=dict(Counter(w.lower() for w in re.findall(r"\w+", open(cwd+"/"+book).read())))
			writer.writerow([counts.get(fieldname,0) for fieldname in text]+
				[punctuation_counts.get(fieldname,0) for fieldname in string.punctuation]+[book.replace(" ", "")]+[person])