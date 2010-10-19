#!/usr/bin/python

"""Search google for relevant urls

This class will return a list of urls from a specified search on google. 
Optionally it can be specified where to look for the query terms in the search
and how many results that should be returned.

Partial list of search parameters for Google: 
http://code.google.com/apis/searchappliance/documentation/64/xml_reference.html
"""

__author__ = 'Henrik Groenholt Jensen'
__version__= '1.0'
__modified__='3-10-2010'

from ListCrawlerBase import ListCrawlerBase
import lxml
import lxml.html
from lxml import etree

import time

class SearchGoogle(ListCrawlerBase):
        
    _results_per_page = "&num=10"
    _search_loc = "&as_occt=any"
    _site = ""    
    
    url = True
    cached_site = False
    summary = False
    title = False
    
    _return_options = [url,cached_site,summary,title]
    
    _results_cache = {}    

    def __init__(self):                
        self.results = []

    # Examplified use of decorater properties:
    # - search.results_per_page (returns 50)
    # - search.results_per_page = 100 (set variable value to 100)
    
    
    #######################
     ## CRAWLER OPTIONS ##
    #######################
    
    @property    
    def results_per_page(self):
        return self._results_per_page

    @property
    def search_location(self):
        return self._search_loc
     
    @property    
    def site(self):
        if len(self._site):
            return self._site
        else: 
            return "Error: No site option set."

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
        @param options: "any","url","body","links" or "title"
        @param type: str
        """
        assert loc=="any" or loc=="url" or loc=="title" or loc=="body" or \
        loc=="links"
        self._search_loc = "&as_occt="+loc
        
    @site.setter
    def site(self,url):
        """ """
        assert isinstance(url,str)
        self._site="&as_sitesearch="+url
    
    ######################
     ## SEARCH RESULTS ##
    ######################
    
    def return_options(self):
        """Get current return options"""
        return [('url',self.url),('cached site',self.cached_site),
                ('summary',self.summary),('title',self.title)]
        
    def _search(self):
        """Search google to get a list of (by default) 50 result urls
        
        @return: Returns a list og google urls in descending order
        @rtype: list of urls
        """
        
        print
        
        search_url = ("http://www.google.com/search?hl=en&lr=lang_en"+self.query+
            self._results_per_page+self._search_loc+"&as_qdr=all"+self._site)
        
        print "Url used for search: "+search_url

        results = self.open_url(search_url)
        
        while not results:
            print 'Google 503-fried us :/'
            print 'Sleeping...'
            time.sleep(900) 
            print 'Woke up! Retrying...'
            results = self.open_url(search_url)
        
        parser = etree.HTMLParser()
        tree = lxml.etree.parse(results, parser)

        result_fields = tree.xpath('//li[@class="g"]')                
        
        print "Found "+str(len(result_fields))+" fields"
        
        search_results={}
        search_results['url'] = []
        search_results['cached_site'] = []
        search_results['summary'] = []
        search_results['title'] = []
        
        for field in result_fields:
        
            if self.url:
                result=field.xpath('h3/a[@class="l"]')
                search_results['url'].append(result[0].get('href'))
                            
            if self.cached_site:
#                print "Accessing potentially cached site..."
                result=field.xpath('div//span[@class="gl"]/a[1]')
#                print "Result from xpath:"
#                print result
                if len(result):
                    if result[0].text=="Cached": 
                        result = result[0].get('href')
#                        print "Found cache..."
                    else: result = ""
                    try:
                        search_results['cached_site'].append(result)
#                        print "Adding to cache.."
#                        print search_results['cached_site']
                    except:
                        search_results['cached_site'] = []
                        search_results['cached_site'].append(result) 
#                        print "Created and added to new cache.."
#                        print search_results['cached_site']
#                print                     
                
            if self.summary:            
                result=field.xpath('div[@class="s"]/text()')
                result="".join(result)
                if isinstance(result,unicode): result.encode('UTF8')                   
                search_results['summary'].append(result)
                
            if self.title:
                result=field.xpath('h3/a[@class="l"]/text()')
                result="".join(result)
                if isinstance(result,unicode): result.encode('UTF8')
                search_results['title'] = []                

        return search_results

    
    def get_results(self,query):
        """Get a list of (be default) 50 urls from a google search 

        @return: Returns a list of googled urls in descending order
        @rtype: list of urls

        @raise KeyError: If no searches have been cached
        """
        
        self.query = "&q="+query.replace(' ','+')        
        
        try:
            results = self._results_cache[self.query]
            if results[1]!=self.return_options():
                self._results_cache[self.query] = (self._search(),self.return_options())
                results = self._results_cache[self.query]
        except KeyError:
            self._results_cache[self.query] = (self._search(),self.return_options())
            results = self._results_cache[self.query]

        return results[0]

