#!/usr/bin/python

"""Name here

Description here
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='16-09-2010'

import urllib2

class ListCrawlerBase(object):
    """Description here"""

    def open_url(self, url):
        """specifics here"""

        request = urllib2.Request(url)
        request.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT "
            "6.1; he; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8")
        request.add_header("Referer", "http://www.google.com")

        return urllib2.urlopen(request)
