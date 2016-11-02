import urllib2
import re


def download(url, user_agent='wswp', num_entries=2):
    print 'Downloading: ', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_entries > 2:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                return download(url, user_agent, num_entries)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)

    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)

    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...

if __name__ == '__main__':
    crawl_sitemap('http://vestajunior.ir/sitemap.xml')
