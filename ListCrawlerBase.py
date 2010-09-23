#!/usr/bin/python

"""Class-extension for crawlers

This module is used by crawlers for opening urls and impersonating a standard
Firefox browser (see BaseCrawler for more info).
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='23-09-2010'

import urllib2
from BaseCrawler import BaseCrawler

class ListCrawlerBase(BaseCrawler):
    """Open a url by calling ListCrawlerBase.open_url(url)"""

    # Nothing yet besides the extended functionalities..
    pass
