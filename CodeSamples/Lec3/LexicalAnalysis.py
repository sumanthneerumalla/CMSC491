import twitter
import json
from collections import Counter
from prettytable import PrettyTable


def removeUnicode(text):
	asciiText=""
	for char in text:
		if( ord(char)  <128):
			asciiText = asciiText + char
	return asciiText

CK = "LipYGLsynELHg8kGXJw9M68h9"
CS = "dM0NW7VAj2t4EHGpOzTKfkpcFSDMaC42IVdZGIT47eLFyMctjs"
token = "945794155-6VFpCWRBZPUFh4IyjGIlejiNiDN4YVmscbLcWE9m"
tokenSecret = "qbtGWl0rKMs76tRr6iZb53uQQOuVSKDDHvxDM95QH76WV"

auth = twitter.oauth.OAuth(token,tokenSecret,CK,CS)

tw = twitter.Twitter(auth=auth)


q = '@twitterapi'
tw = twitter.Twitter(auth=auth)
count = 10
tweets= tw.search.tweets(q=q,count=count,lang='en')
texts = []
for status in tweets["statuses"]:
	texts.append(status["text"])
print "============================CREATING A BAG OF WORDS============================================="
words = []
for text in texts:
	for w in text.split():
		words.append(w)

print words

cnt = Counter(words)

pt = PrettyTable(field_names=['Word','Count'])
srtCnt = sorted(cnt.items(),key=lambda pair: pair[1],reverse=True)
for kv in srtCnt:
	pt.add_row(kv)
	
print pt
print "============================LEXICAL DIVERSITY=============================="
print 1.0*len(set(words))/len(words)
