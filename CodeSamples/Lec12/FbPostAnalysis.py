import facebook
import json
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

def removeUnicode(text):
    asciiText = ""
    for char in text:
        if(ord(char) < 128):
            asciiText = asciiText + char
    return asciiText

def count_likes(id, fb_conn):
    cntLikes= 0
    print "\n\nin count likes, id is ", id
    edge = fb_conn.get_object('/' + id + '/likes', limit = 1,summary='True')
    return (edge['summary']['total_count'])

ACCESS_TOKEN = 'EAACEdEose0cBAKLlD2RfIHvqFN1gLa4wUyRfeYPAiXd7Pg8jRKoj7FDQ0wyzT4hTyRdeOFgHOeZBDCfahoREccmtHqak4QriedArU1P1a4WB2ycxbbTsLPog6ARd4i4ydSbxMCdL5fLSPwhIz47ZBpZAxylItng9COwBEaQkAZDZD'

fb = facebook.GraphAPI(ACCESS_TOKEN)
d_id = fb.request('search', {'q':'Greta Garbo', 'type': 'page', 'limit':5})
print d_id

Greta = '17287115271'

d_posts = fb.get_connections(Greta, connection_name ='posts')
print "Greta posts", len(d_posts)
print "Len of D posts is ", len(d_posts['data'])

with open('gPost.txt', 'w') as f:
    f.write(str(d_posts))
    f.close()

for post in d_posts['data']:
    print post['message'].encode('utf-8')
    if 'id' in post:
        print "has id number ", post['id'],
        print " and like count ", count_likes(post['id'], fb)
    else:
        with open('no_obj.txt', 'a') as o:
            o.write(str(d_posts))
            o.close
    print "---"


print "\n The first comment is  \n", d_posts['data'][1]['comments']['data'][0]

pepsi_id = 'PepsiUS'
coke_id = 'CocaCola'
Hillary = '889307941125736'
Donald = '153080620724'

print "Greta likes: \t %d"%(fb.get_object(Greta)['likes'])
print "Coke likes: \t %d"%(fb.get_object(coke_id)['likes'])
print "Pepsi likes: \t %d"%(fb.get_object(pepsi_id)['likes'])
print "Donald likes: \t %d"%(fb.get_object(Donald)['likes'])
print "Hillary likes: \t %d"%(fb.get_object(Hillary)['likes'])

vs_tot = 0
vs_pos = 0
vs_neg = 0
num_cnt = 0
likes = ""
for dataItem in d_posts['data'][1]['comments']['data']:
    print removeUnicode(dataItem['message'])
    for datas in dataItem:
        if datas == 'from':
            gmrFrom = ''
            for cmtName in dataItem['from']:
                gmrFrom = gmrFrom + dataItem['from'][cmtName].encode('utf-8')+ ":"
                gmrFrom = '----FROM: ' + gmrFrom
        if datas == 'like_count':
            likes  = "----Like Count" + str(dataItem['like_count'])
        print gmrFrom
        print likes

vs = vaderSentiment(dataItem['message'].encode('utf-8'))
print "----Sentiment : " + str(vs['compound'])
vs_tot = vs_tot + vs['compound']
num_cnt = num_cnt + 1
if vs['compound'] < 0:
    vs_neg = vs_neg + 1
else:
    vs_pos = vs_pos + 1