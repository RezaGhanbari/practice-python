from crawler import *
import re

url = 'http://example.webscraping.com/view/UnitedKingdom-239'
headers = {}
html = download(url, headers=headers, proxy=None, num_retries=5)
print re.findall('<td class="w2p_fw">(.*?)</td>', html)
# print re.findall('<td class="w2p_fw">(.*?)</td>', html)[1]
