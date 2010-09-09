

import urllib2
import re
import lxml
import lxml.html
from lxml import etree
import random
import time
import urlparse


class Crawler(object):

    #def __init__(self)


    def parse(self, baseurl, pages=lambda: ['0'] + [chr(x) for x in range(65,90)]):

        pages = lambda : ['0']

        for page in pages():


            url = baseurl + page

            request = urllib2.Request(url)
            request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8")
            request.add_header("Referer", "http://www.google.com")

            html = urllib2.urlopen(request)
            #html = open("test.xml")

            parser = etree.HTMLParser()
            
            tree = lxml.etree.parse(html, parser)
            #print etree.tostring(tree)

            #links = tree.xpath("//div[id=result-box]/ul/li/a")
            links = tree.xpath("//div[@id='result-box']/ul/li/a")
            #/html/body/div/div[8]/div/ul/li[7]/a
            for link in links:
                print link.text, link.get("href")
                random.seed(time.time())
                time.sleep(random.randrange(3, 6))

                page_url_base = "http://www.orpha.net/consor/cgi-bin/"

                page_url = urlparse.urljoin(page_url_base, link.get("href"))
                
                page_request = urllib2.Request(page_url)
                page_request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8")
                page_request.add_header("Referer", "http://www.google.com")

                f = file(link.text, 'w')
                f.write(urllib2.urlopen(page_request).read())
                f.close()

                #page_tree = lxml.etree.parse(page_html, parser)

        

    
class WebsiteInterface(object):

    
    def __get__(self):
        raise NotImplemented

    def __set__(self, val):
        raise NotImplemented


if __name__ == "__main__":
    crawler = Crawler()
    crawler.parse('http://www.orpha.net/consor/cgi-bin/Disease_Search_List.php?lng=EN&TAG=')
