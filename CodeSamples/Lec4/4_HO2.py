import json
import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://twitter.com/search?q=%40twitterapi&src=typd"
html = requests.get(url).text
soup = BeautifulSoup(html,'html5lib')
fpText = soup.p.text
print fpText
allParas = soup.find_all('p')

for para in allParas:
	print para.text.encode('utf-8')

q = "@twitterapi"
count = 100
for status in tw.search.twets(q=q,coun=count)["statuses"]:
	if status["lang"] =='en':
		print json.dumps(status["text"]).encode('utf-8')
