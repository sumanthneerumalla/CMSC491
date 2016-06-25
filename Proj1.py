import twitter
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

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

def getTweets(query,num):
    results = []
    while (len(results) < 25):
        gmrPycon = tw.search.tweets(q=query,lang='en')
        for status in gmrPycon["statuses"]:
            results.append(removeUnicode(status["text"]))
    return results[0:num]

def getLexicalDiversity(someString):
    words = someString.split()
    numUnique = len(set(words))
    numTotal = len(words)
    return ((1.0 * numUnique)/numTotal)

def tweetPrinter(arrayOfTweets):
    for each in range(0,len(arrayOfTweets)):
        print "Tweet number",each + 1,": (Lexical Diversity: ",getLexicalDiversity(arrayOfTweets[each]),", Vader Sentiment Score: ",vaderSentiment(arrayOfTweets[each])['compound']," )", arrayOfTweets[each]

#Search
CocaColaTweets = getTweets("Coca Cola",25)
PepsiColaTweets = getTweets("Pepsi Cola",25)

print "============================= COCA COLA TWEETS =============================="
tweetPrinter(CocaColaTweets)
print "\n\n\n============================= PEPSI COLA TWEETS=============================="
tweetPrinter(PepsiColaTweets)