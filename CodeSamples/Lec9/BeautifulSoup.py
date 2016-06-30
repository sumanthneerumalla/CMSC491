import requests
import html5lib
from bs4 import BeautifulSoup

html = open("Test.htm","r")
print type(html)

soup = BeautifulSoup(html,'html5lib')
print type(soup)

fp_text = soup.p
fa_text = soup.a.text
ftd_text = soup.td.text
div_text = soup.div.text

print fp_text.encode('utf-8'),fa_text.encode('utf-8')
print soup.p.name,soup.a.name
print soup.a.attrs,soup.a['href']
print "P text is ",soup.p.text
print "TD is ",ftd_text
print "div is ", soup.div.text

#get info using the find function

fp_text = soup.find("p")
fa_text = soup.find("a")
ftd_text = soup.find("td")

div_text = soup.find("div")


print "P is ", fp_text
print "TD is ", ftd_text
print "div is", div_text
print " a is", fa_text

bs4_text = soup.find(text="Beautiful Soup")
print "Beautiful Soup is ", bs4_text

#searching for the first tag with a specific id

submit_id =  soup.find(id="sb_form_go")
print submit_id


#searching attributes using find function

stySearch = soup.find(style="display:none")
print stySearch

#search for all strings nd al text in a type of tag
fp_all = soup.find_all("a")
for fp in fp_all:
    print fp.string, "======AND=======", fp.text.encode('utf=8')