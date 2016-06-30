def gmrTraverse(gmrText, gmrDict, level):
	for key in gmrDict:
		print gmrText, key
		if isinstance(gmrDict[key], dict):
			print '                                                          entered dict'
			text = "    "*level + " " + str(key)
			level = level + 1
			gmrTraverse(text, gmrDict[key], level)
			level = level - 1
		if isinstance(gmrDict[key], list)and gmrDict[key] is not None:
			print '                                                           entered list'
			lstDict = {}
			for i, item in enumerate(gmrDict[key]):
				lstDict[i] = item
				#print gmrText, key, i, item 
			text = "    "*level + str(key)
			level = level + 1
			gmrTraverse(text, lstDict, level)
			level = level - 1	
		
test_str = open("gmrTweets.txt").read()
print test_str[0]
test_dic = eval(test_str)
gmrTraverse("", test_dic, 1)

# to get the second index value in entities, urls, indices
print test_dic["entities"]["urls"][0]["indices"][0]
