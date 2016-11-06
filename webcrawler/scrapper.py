from crawler import *
import re

url = 'http://example.webscraping.com/view/UnitedKingdom-239'
headers = {}
html = download(url, headers=headers, proxy=None, num_retries=5)
print re.findall('<td class="w2p_fw">(.*?)</td>', html)
# print re.findall('<td class="w2p_fw">(.*?)</td>', html)[1]

# more robust item
# re.findall('<tr id="places_area__row"><td class="w2p_fl">
# <label for="places_area" id="places_area__label">
# Area: </label></td><td class="w2p_fw">(.*?)</td>', html)
