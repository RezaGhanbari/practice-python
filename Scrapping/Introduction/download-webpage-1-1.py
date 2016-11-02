import urllib2

print lambda url: urllib2.urlopen(url).read()