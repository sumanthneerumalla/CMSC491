from bs4 import BeautifulSoup
import requests
import json
import codecs
import nltk
nltk.download('punkt')

def removeUnicode(text):
    asciiText=""
    for char in text:
        if( ord(char)  <128):
            asciiText = asciiText + char
    return asciiText


fileObj = codecs.open("Clearing.rtf","w","UTF")
html = requests.get("http://www.reuters.com/article/us-china-yuan-payments-exclusive-idUSKBN0M50BV20150309")
soup = BeautifulSoup(html.text,'html5lib')

all_paras = soup.find_all('p')


#write text to file and collate it into a str var
data_2016 = ""
for para in all_paras:
    fileObj.write(para.text)
    data_2016 = data_2016 + para.text
asc_2016 = removeUnicode(data_2016)

#g444hhhhet a list of sentences

lstSent = nltk.tokenize.sent_tokenize(asc_2016)
print type(lstSent),"sent type"

#Get a list of words by tokenizing our sentnences
#need list of individual words for frrequency distribution calc
words = []
for sentence in lstSent:
	for word in nltk.tokenize.word_tokenize(sentence):
		words.append(word.lower())

#Get the frquency distribution
frqDist = nltk.FreqDist(words)
print "dfeq", type(frqDist)

#Now calculate and print stats
word_cnt = 0
for item in frqDist.items():
	word_cnt = word_cnt + item[1]
unique_word_cnt = len(frqDist.keys())

#Words that appear only once are called hapaexes
hapaxNo = len(frqDist.hapaxes())

#make list of stop words to not consider iin analysis
skips = ["and", ".", "to", ",", "the", "for", "in", "of", "that", "a", "on", "is", "get", "you", "has", "as", "at", "are", "'", "an", "with", "will", "not", "have", "would", "so", '"', "but", ":", "be", "like", "if", "should", "also", "there", "or", "by", "per"]

#Get a list of tuples of the most frequent words
#notice you should use w[0] fo compare with skips
mostFreq = []
for w in frqDist.items():
	if w[0] not in skips:
		mostFreq.append(w)

#Print out our findings
print "Hillary Economic Platofmr"
print 'Num lstSent:'.ljust(25), len(lstSent)
print 'Num Words:'.ljust(25), word_cnt
print 'Num Unique Words:'.ljust(25), unique_word_cnt
print 'Num Hapaxes:'.ljust(25), hapaxNo
print "The most frequent words follow"

#sort on count
mostFreq.sort(key=lambda c: c[1])

#Print out words and their frquency off occuance
#But only print out the highest ten in the list
for w in mostFreq[-10:]:
	print w[0].encode('utf-8'), " \thas a count of ", w[1]


#CHUNKING AND EXTRACTION

#Now get the POS for the words collection
#pos_tag takes a list as input
#create word list for each sentence (for context) not inddivul word list
#then inut that
sentWords = [nltk.tokenize.word_tokenize(s) for s in lstSent]
posWords = [nltk.pos_tag(w) for w in sentWords]
posWords = [token for sent in posWords for token in sent]
for (token, pos) in posWords:
    print token, pos

#Now we will use Russell's algorithm for chunking
#first we will get a collector for all our chunk
chunkCollector = []

#Then one for the chunk we have just collected
foundChunk = []

#Keep track of last part-of-speech
lastPos = None

#Now the analysis
for (token, pos) in posWords:
	#check to see if multiple NNs are in sequence
	if pos == lastPos and pos.startswith('NN'):
 		foundChunk.append(token)
	elif pos.startswith('NN'):
		#here we have a control break in chunks
		if foundChunk != []:
			#here, something in hopper so add to collection
			chunkCollector.append((' '.join(foundChunk), pos))
		#In anycase, on control break, reset foundChunk
		foundChunk = [token]
	#Reset lastPos to currentPos
	lastPos = pos

#now convert to a dictionary and count frequunecy for each chunk
dChunk = {}
for chunk in chunkCollector:
	dChunk[chunk] = dChunk.get(chunk, 0) + 1

print "for Hillary Clinton Economic Policy"
for (entity, pos) in dChunk:
	if entity.istitle():
		print '\t%s (%s)' % (entity, dChunk[entity, pos])

