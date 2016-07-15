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

targetURL = "http://www.ecommercetimes.com/story/52616.html"
page = requests.get(targetURL)
pageSoup = BeautifulSoup(page.text,'html5lib')
articleSoup = pageSoup.find_all("p")

articleText = ""
for eachPar in articleSoup:
    if (eachPar.string) != None:
        articleText = articleText + eachPar.text
articleAscii = removeUnicode(articleText)

sentences = nltk.tokenize.sent_tokenize(articleAscii)
words = []
for sentence in sentences:
    