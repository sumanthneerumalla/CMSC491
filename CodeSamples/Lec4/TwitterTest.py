import twitter

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

#Search
gmrPycon = tw.search.tweets(q="#Hillary2016")
for status in gmrPycon["statuses"]:
	print removeUnicode(status["text"])
print "==========="
