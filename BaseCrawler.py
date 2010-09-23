#!/usr/bin/python

"""Class-extension for crawlers

So far:
~~~~~~~
This module is used by crawlers for opening urls and impersonating a standard
Firefox browser.

It is extended by ListCrawlerBase
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='23-09-2010'

import urllib2

class BaseCrawler(object):
    """So far only used for opening urls"""

    def __init__(self,query):
        pass

    def open_url(self, url):
        """
        @param url: url used to access the specific page
        @type url: str

        @return: Returns a handle for the specific url
        @rtype: instance of urllib2.urlopen()

        @raise URLError: If the page is not recognized
        """
    
        request = urllib2.Request(url)
        request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT "
            "6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8")
        request.add_header("Referer", "http://www.google.com")
    
        try:
            print type(urllib2.urlopen(request))
            return urllib2.urlopen(request)
        except Exception as e:
            print "Could not open url"
            raise e
