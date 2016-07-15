from bs4 import BeautifulSoup
import requests
import nltk
nltk.download('punkt')


def removeUnicode(text):
    asciiText=""
    for char in text:
        if( ord(char)  <128):
            asciiText = asciiText + char
    return asciiText

#use requests library to get page from url
targetURL = "http://www.ecommercetimes.com/story/52616.html"
page = requests.get(targetURL)

#use BeautifulSoup to get navigable parse tree and get article text from page
pageSoup = BeautifulSoup(page.text,'html5lib')
articleSoup = pageSoup.find_all("p")

articleText = ""
for eachPar in articleSoup:
    if (eachPar.string) != None:
        articleText = articleText + eachPar.text
articleAscii = removeUnicode(articleText)

#tokenize words and sentences
sentences = nltk.tokenize.sent_tokenize(articleAscii)
words = []
for sentence in sentences:
    for word in nltk.tokenize.word_tokenize(sentence):
        words.append(word.lower())



#Calculate the frquency distribution
frqDist = nltk.FreqDist(words)

word_cnt = 0
for item in frqDist.items():
    word_cnt = word_cnt + item[1]
unique_word_cnt = len(frqDist.keys())

hapaxNo = len(frqDist.hapaxes())

skips = ["and", ".", "to", ",", "the", "for", "in", "of", "that", "a", "on", "is", "get", "you", "has", "as", "at", "are", "'", "an", "with", "will", "not", "have", "would", "so", '"', "but", ":", "be", "like", "if", "should", "also", "there", "or", "by", "per"]

mostFreq = []
for w in frqDist.items():
    if w[0] not in skips:
        mostFreq.append(w)

#Print out statistics
print "Article Statistics"
print 'Num Sentences:'.ljust(25), len(sentences)
print 'Num Words:'.ljust(25), word_cnt
print 'Num Unique Words:'.ljust(25), unique_word_cnt
print 'Num Hapaxes:'.ljust(25), hapaxNo
print "The most frequent words follow"

mostFreq.sort(key=lambda c: c[1])
for w in mostFreq[-10:]:
    print w[0].encode('utf-8'), " \thas a count of ", w[1]


#Print out Parts of Speech
sentWords = [nltk.tokenize.word_tokenize(s) for s in sentences]
posWords = [nltk.pos_tag(w) for w in sentWords]
posWords = [token for sent in posWords for token in sent]
for (token, pos) in posWords:
    print token, pos

#Chunking
chunkCollector = []
foundChunk = []
lastPos = None

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

#Convert to a dictionary and count for each chunk
dChunk = {}
for chunk in chunkCollector:
    dChunk[chunk] = dChunk.get(chunk, 0) + 1

print "\nChunking"
for (entity, pos) in dChunk:
    if entity.istitle():
        print '\t%s (%s)' % (entity, dChunk[entity, pos])


#Create 3 sentence summary from article text
#This portion did not work with the 'russel.pyc' component that was on blackboard so it is being commented out
#
# import russel as ru
# articleSum = ru.summarize(articleText)
# print "Summary of Article"
# print "Three Sentence Summary"
# for each in articleSum['top_n_summary']:
#     print removeUnicode(each)