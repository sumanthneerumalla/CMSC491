test_str = open("gmrTweets.txt").read()
dic = eval(test_str)
print dic['text']
for key in dic:
	print key,dic[key]
for key in dic:
	print key,isinstance(dic[key],dict)

