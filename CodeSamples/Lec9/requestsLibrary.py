import requests
import html5lib
from bs4 import BeautifulSoup

URL = "https://www.theclearinghouse.org/payments/chips"
webpage = requests.get(URL)
print type(webpage)