from bs4 import BeautifulSoup
import requests

r = requests.post(url=raw_input('Please insert a valid url:\n'))
s = BeautifulSoup(r.text, 'lxml')
# broken_html = raw_input('paste the
# parse the html
fixed = s.prettify()
s = fixed.encode('ascii', 'ignore')
f1 = open('./testfile.txt', 'w+')
f1.write(s)
