import requests
import json

AT = "EAACEdEose0cBAPhjhh3GQg0yiTbshy2SM8V4PkN8AKaTwyzH9jRWNaENy7TpWpUFBZAVpp4XGQENZAwbjQxnmDrs5xFMOYfb0yz1ni59vZAuTq9RbYorHuX2z9buXv3TgTxfQwEe5lWpdmqQbK4ZC0s9U4RmrsMWETgPV57SrwZDZD"
fb_url = 'https://graph.facebook.com/me'
fields = 'id,name'
url = '%s?fields=%s&access_token=%s'%(fb_url,fields,AT)
results = requests.get(url).json()
print json.dumps(results,indent=1)