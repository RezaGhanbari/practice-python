import sys
from link_crawler import *
import urllib2
import urlparse


def link_crawler_two(seed_url, link_regx):
    """"
    Crawl from the given seed URL following links matched by link_regx
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regx, link):
                link = urlparse.urljoin(seed_url, link)
                crawl_queue.append(link)