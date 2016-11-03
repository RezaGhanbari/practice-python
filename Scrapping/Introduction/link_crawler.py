import re
import urllib2


def download(url, user_agent='wswp', num_entries=2):
    """
    :param url:
    :param user_agent:
    :param num_entries:
    :return:
    """
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


def get_links(html):
    """
    Return a list of links from html
    :param html:
    :return:
    """
    # A regular expression to extract all links from the web page
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)

    # List of all links from the web page
    return webpage_regex.findall(html)


def link_crawler(seed_url, link_regx):
    """
    crawl from the given seed URL following links matched by link_regx
    :param seed_url:
    :param link_regx:
    :return:
    """
    crawl_queue = [seed_url]
    url = crawl_queue.pop()
    html = download(url)
    # filter for links matching our regular expression
    for link in get_links(html):
        if re.match(link_regx, link):
            crawl_queue.append(link)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com',
                 'example.webscraping.com/(index|view)/')
