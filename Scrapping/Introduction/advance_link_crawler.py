from link_crawler import *
import urlparse


def link_crawler(seed_url, link_regx):
    """
    :param seed_url:
    :param link_regx:
    :return:
    """
    crawl_queue = [seed_url]

    # keep track which URL's have seen before
    seen = set(crawl_queue)

    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):

            # check if link matches expected regex
            if re.match(link, link_regx):
                # from absolute link
                link = urlparse.urljoin(seed_url, link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

if __name__ == '__main__':
    link_crawler('http://example.webscraping.com',
                 'example.webscraping.com/(index|view)/')
