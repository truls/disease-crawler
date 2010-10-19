#!/usr/bin/python

"""name

description
"""

__author__ = 'Henrik Groenholt Jensen, Truls Asheim and Michael Andersen'
__version__= '1.0'
__modified__='23-09-2010'

from ListCrawlerBase import ListCrawlerBase
import lxml
import lxml.html
from lxml import etree

from SearchGoogle import SearchGoogle
import random
import time
import re

class OrphanetCrawler(SearchGoogle):

    count=0
    run=0

    def __init__(self):
        pass

    def crawl_url(self,url):
        
        print "========== NEW QUERY BEGUN ============"
        
        url="\""+url+"\""
        
        # Set GoogleCrawler options
        self.url = False
        self.cached_site = True
        self.site = "orpha.net"
        
        # Search Google        
        urls = self.get_results(url)                
        
        orpha_link = None        
        flag = False
        for cached_site in urls['cached_site']:
            if "Disease_Search.php" in cached_site and not flag: flag = True
            if "cgi-bin/OC_Exp.php" in cached_site and not flag: flag = True
            if flag: 
                orpha_link = cached_site
                print "Orphanet url found"
                break
        
        if flag:
            self.count+=1
            self.run+=1
        else: self.run+=1        
        
        print "~~~~~~~~~~"
        print "Percentage found: "+str(float(self.count)/self.run)
        print "Run: "+str(self.run)
        print "~~~~~~~~~~"
        
        if orpha_link:
        
            print orpha_link
            opened_url = self.open_url(orpha_link)
        
            parser = etree.HTMLParser()
            
            tree = lxml.etree.parse(opened_url, parser)
            
            disease_info=tree.xpath('//td[@class="twoColumnsTable"]//tr/td//text()')
#            disease_info=tree.xpath('//text()') 

            print disease_info            
#            disease_info=[e for e in disease_info if not '\n' in e]
            sanitizer = re.compile('[\W]')
            disease_info=[sanitizer.sub(' ', e) for e in disease_info]
            print disease_info
            
            # Notice prevalence is left out due to parsing problems
            tokens=["Orpha number\r","Inheritance","Age of onset","ICD 10 code\r","MIM number\r","Synonym(s)"]
            token_indices=[disease_info.index(e) for e in tokens]
            assert len(token_indices)==6
            results={}
            results["Orpa number"]=disease_info[token_indices[0]+1:token_indices[1]-1]
            results["Inheritance"]=disease_info[token_indices[1]+1:token_indices[2]-1]
            results["Age of onset"]=disease_info[token_indices[2]+1:token_indices[3]-1]
            results["ICD 10 code"]=disease_info[token_indices[3]+1:token_indices[4]-1]
            results["MIM number"]=disease_info[token_indices[4]+1:token_indices[5]-1]
            results["Synonyms"]=disease_info[token_indices[5]:]
            
            print results
            
            disease_summary=tree.xpath('//div[@class="article"]/p[1]')[0].text
            
        time.sleep(1)
            
        
        
