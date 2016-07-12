import facebook
import json

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

ACCESS_TOKEN = 'EAACEdEose0cBAPhjhh3GQg0yiTbshy2SM8V4PkN8AKaTwyzH9jRWNaENy7TpWpUFBZAVpp4XGQENZAwbjQxnmDrs5xFMOYfb0yz1ni59vZAuTq9RbYorHuX2z9buXv3TgTxfQwEe5lWpdmqQbK4ZC0s9U4RmrsMWETgPV57SrwZDZD'

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








