#!/usr/bin/python

"""Get a list of urls to parse data from

Instantiates a predefined crawler module and returns a list of urls to parse
data from
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='16-09-2010'

import GoogleListCrawler
import OrphanetListCrawler

class ListCrawler(object):

    crawler=None
    lst=[]

    def __init__(self, page, query=None): 
        """Specify page - query is used for google only

        @param page: Specifies what crawler module to be used
        @type page: str

        @param query: Only relevant for the 'google'-crawler
        @type query: str

        @raise NotImplemented: If the page is not recognized
        """       
        assert isinstance(page,str)
        assert isinstance(query,str)

        self.page = page
        self.query = query

        if 'google' in page.lower():
            self.crawler = GoogleListCrawler

        if 'orphanet' in page.lower():
            self.crawler = OrphanetListCrawler

        if self.crawler is None:
            print 'Crawler:', page 
            raise NotImplemented

    def get():
        """         
        @return: Returns a list of urls
        @rtype: list
        """
        
        crawler = self.crawler()

        return crawler.get_results(self.query)


