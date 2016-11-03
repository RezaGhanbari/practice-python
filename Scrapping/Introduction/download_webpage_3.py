"""
Here is an updated version of our download function
with the default user agent set to 'wswp' which
stands for Web Scraping with Python
"""
# Now we have a flexible download function
# that can be reused in later examples to
# catch errors, retry the download
# when possible, and set the user agent.

import urllib2


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
