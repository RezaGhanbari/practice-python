import itertools as it
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


# maximum number of consecutive download errors allowed
max_errors = 5

# minimum number of consecutive download errors
num_errors = 0

for page in it.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)

    if html is None:
        # received an error trying to download this webpage
        num_errors += 1
        if num_errors == max_errors:
            # reached maximum number of
            # consecutive errors so exit
            break
    else:
        # success - can scrape the result
        # ...
        num_errors = 0
        