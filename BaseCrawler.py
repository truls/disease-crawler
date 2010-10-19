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

import cookielib
import os.path

import time

class BaseCrawler(object):
    """So far only used for opening urls"""

    _counter=0

    _referer="http://www.google.com"
    
    COOKIEFILE = 'cookies.lwp'
    cj = None

    def __init__(self,query):
        pass

    def set_referer(self,referer):
        assert isinstance(referer,str)
        self._referer=referer

    def open_url(self, url):
        """
        @param url: url used to access the specific page
        @type url: str

        @return: Returns a handle for the specific url
        @rtype: instance of urllib2.urlopen()

        @raise URLError: If the page is not recognized
        """
        
        self._counter+=1
        
        urlopen = urllib2.urlopen
        Request = urllib2.Request
        self.cj = cookielib.LWPCookieJar()
        
#        if os.path.isfile(self.COOKIEFILE):
#            self.cj.load(self.COOKIEFILE)
         
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(opener)
#        headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)"}
#        headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10"}
#        headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)" }
#        headers = {"User-Agent" : "Opera/9.70 (Linux ppc64 ; U; en) Presto/2.2.1" }
#        headers = {"User-Agent" : "Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12" }
#        headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)" }
        
        
        if self._counter>10000:
            headers = {"User-Agent" : "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)" }
        elif self._counter>30000:            
            headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)" }    
        else:
            headers = {"User-Agent" : "Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12" } 
    
        try:
            req = Request(url, None, headers)
            handle = urlopen(req)
        except:
            handle=None
#        except IOError, e:
#            print 'We failed to open "%s".' % url
#            if hasattr(e, 'code'):
#                print 'We failed with error code - %s.' % e.code
#            elif hasattr(e, 'reason'):
#                print "The error object has the following 'reason' attribute :"
#                print e.reason
#                print "This usually means the server doesn't exist,',"
#                print "is down, or we don't have an internet connection."
#            raise e
            
#        else:
#            print 'Here are the headers of the page :'
#            print handle.info()
            
        print
        
        if self.cj: self.cj.save(self.COOKIEFILE)
        else: "Could not save cookie"
        
        return handle
