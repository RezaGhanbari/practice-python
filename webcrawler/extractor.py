from crawler import *
from bs4 import BeautifulSoup

url = 'http://rezaghanbari.ir/'
headers = {}
html = download(url, headers, proxy=None, num_retries=5)
soup = BeautifulSoup(html, "lxml")

# locate the area row
tr = soup.find(attrs={'class':'container'})
td = tr.find(attrs={'class':'logo'}) # locate the area tag
area = td.text # extract the text from this tag
print area