#!/usr/bin/python

"""Search google for relevant urls

This class will return a list of urls from a specified search on google. 
Optionally it can be specified where to look for the query terms in the search
and how many results that should be returned.

Partial list of search parameters for Google: 
http://code.google.com/apis/searchappliance/documentation/64/xml_reference.html
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='23-09-2010'

from ListCrawlerBase import ListCrawlerBase
import lxml
import lxml.html
from lxml import etree

class GoogleListCrawler(ListCrawlerBase):
        
    _results_per_page = "&num=50"
    _search_loc = "&as_occt=any"
    results_cache={}

    def __init__(self,query):        
        self.query = "&q="+query
        self.results = []

    # Examplified use of properties:
    # - search.results_per_page (returns 50)
    # - search.results_per_page = 100 (set variable value to 100)
    
    @property    
    def results_per_page(self):
        return self._results_per_page

    @property
    def search_location(self):
        return self._search_loc

    @results_per_page.setter
    def results_per_page(self, num):
        """        
        @param num: Set the number of results per page
        @param type: int
        """
        assert isinstance(num,int)
        assert num>=0 and num<=999
        self._results_per_page = "&num="+str(num)

    @search_location.setter
    def search_location(self,loc="any"):
        """        
        @param loc: Specifiy where to look for query terms. "any" by default.
        Possible options are: "any","url","body","links" or "title"
        @param type: str
        """
        assert loc=="any" or loc=="url" or loc=="title" or loc=="body" or \
        loc=="links"
        self._search_loc = "&as_occt="+loc
    

    def search(self):
        """Search google to get a list of (by default) 50 result urls
        
        @return: Returns a list og google urls in descending order
        @rtype: list of urls
        """
        
        self.search_url = ("http://www.google.com/search?hl=en"+self.query+
            self._results_per_page+self._search_loc+"&as_qdr=all")

        results = self.open_url(self.search_url)

        parser = etree.HTMLParser()
        tree = lxml.etree.parse(results, parser)

        links=tree.xpath('//h3/a[@class="l"]')

        return [url.get("href") for url in links]        

    
    def get_results(self):
        """Get a list of (be default) 50 urls from a google search 

        @return: Returns a list of googled urls in descending order
        @rtype: list of urls

        @raise KeyError: If no searches have been cached
        """

        try:
            self.results = self.results_cache[self.query]
        except KeyError:
            self.results_cache[self.query] = self.search()
            self.results = self.results_cache[self.query]

        return self.results

