import twitter
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import sentiment
import json
import requests
import facebook
import russell as ru
import codecs
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment


def removeUnicode(text):
    asciiText = ""
    for char in text:
        if (ord(char) < 128):
            asciiText = asciiText + char
    return asciiText


def count_likes(id, fb_conn):
    cntLikes = 0
    edge = fb_conn.get_object('/' + id + '/likes', limit=1, summary="true")
    return (edge["summary"]["total_count"])


consumer_key = "BziIwaK6XQDdStrR4FsrJSieY"
consumer_secret = "a1xvk9XGvN4Tq5ZnA5et9NasEgAY2LoUQebqXTqx8pB5QqMg2H"
oauth_token = "3214717593-TUH2kQYqyDE6zEhfX3suwiYimT6zA9gaRyMKa5F"
oauth_secret = "0AXIV614eZ7nvpTtHo8taWJ2m8yf4OFiK8LNIwMuMHMjR"

skips = set(stopwords.words('english'))
skips |= set(['""', "''", ' ', '-', ' - '])
q = "#realDonaldTrump"
count = 25

auth = twitter.oauth.OAuth(oauth_token, oauth_secret,
                           consumer_key, consumer_secret)

tw = twitter.Twitter(auth=auth)

search = tw.search.tweets(q=q, count=count, lang='en')
statuses = search['statuses']

overall_sentiment = 0.0

def getLexicalDiversity(someString):
    words = someString.split()
    numUnique = len(set(words))
    numTotal = len(words)
    return ((1.0 * numUnique)/numTotal)

for status in statuses:
    corpus = []
    for w in status['text'].split():
        w = removeUnicode(w)
        if w in skips: continue
        if 'http' in w: continue
        if '&amp;' in w: continue
        if '&gt;' in w: continue
        if 'RT' in w: continue
        corpus.append(w)
    unique = set(corpus)
    senti = sentiment(status['text'].encode('utf-8'))
    overall_sentiment += float(senti['compound'])
    print "User:", status['user']['screen_name']
    print "Favorite Count:", str(status['favorite_count'])
    print "Tweet:", removeUnicode(status['text'])
    print "Lexical Diversity: ", getLexicalDiversity(removeUnicode(status['text']))
    print "Retweet Count: ", status['retweet_count']
    print "Compound Sentiment:", senti['compound']
    print "Corpus:"
    for w in corpus: print '\t' + w
    print "Unique tokens:"
    for w in unique: print '\t' + w
    print "-----"

print "Sentiment Summation: %f" % overall_sentiment

print "***********Summary*******************"

fileObj = codecs.open("DT_Platform.rtf", "w", "UTF")
html = requests.get("https://donaldjtrump.com/positions/tax-reform")
soup = BeautifulSoup(html.text, "html5lib")
all_paras = soup.find_all('p')

data_trump = ""

for para in all_paras:
    fileObj.write(para.text)
    data_trump = data_trump + para.text

trump_sum = ru.summarize(data_trump)

print "Summary of Trump tax reform: "
for sent in trump_sum['top_n_summary']:
    print removeUnicode(sent)

articleAscii = removeUnicode(data_trump)
words = []

#num_Co is the number of collocations to find
N=25

#need list of Words by sentence
sentences = nltk.tokenize.word_tokenize(articleAscii)
for sentence in sentences:
    for word in nltk.tokenize.word_tokenize(sentence):
        words.append(word.lower())

#print bigWords

#let's have the nltk analyze our sentWords for collocations
search = nltk.BigramCollocationFinder.from_words(sentences)

#filter out collocations that do not occur at least 2 times
search.apply_freq_filter(2)

#Filter out collocations that have stopwords
search.apply_word_filter(lambda skip: skip in skips)

#We use the Jaccard Index to find our bigrams
#idxJaccard = nltk.metrics.BigramAssocMeasures.jaccard
from nltk import BigramAssocMeasures
idxJaccard = BigramAssocMeasures.jaccard
bigrams = search.nbest(idxJaccard, N)

print "#================================="
print "Bigrams"
for bigram in bigrams:
    print str(bigram[0]).encode('utf-8'), " ", str(bigram[1]).encode('utf-8')


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


print "***********Facebook Posts**************"

ACCESS_TOKEN = 'EAACEdEose0cBANmtjyGTYHxxnzUpoHTFhokpoA8fREXwMe7ZALdpU1oDCEDqKxPteREuPk2GWFNFETh1SbGRpd3D4QAeVCUK3k88zzOVZC5o6XwmdgTCGoQLn3frwoO92Bk1DOuBd6iZCX6nUaY4IS82zK8VNbTTK2y1A8xLwZDZD'

fb = facebook.GraphAPI(ACCESS_TOKEN)

d_id = fb.request('search', {'q': 'Donald Trump', 'type': 'page', 'limit': 5})

# print d_id

Trump = '153080620724'

d_posts = fb.get_connections(Trump, connection_name='posts')

print "Trump posts", len(d_posts)

print "len of D posts is ", len(d_posts['data'])

with open('tPost.txt', 'w') as f:
    f.write(str(d_posts))
    f.close()

for post in d_posts['data'][:10]:
    print post['message'].encode('utf-8')
    print "Sentiment Analysis: ", vaderSentiment(post['message'].encode('utf-8'))['compound']
    print "Lexical Diversity: ", getLexicalDiversity(post['message'].encode('utf-8'))
    if 'id' in post:
        print "has id number ", post['id']
        print " and has like count ", count_likes(post['id'], fb)
    else:
        with open('no_obj.txt', 'a') as o:
            o.write(str(d_posts))
            o.close
    print "---"
