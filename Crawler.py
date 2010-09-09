
from ParserInterface import ParserInterface
from OrphaNet import OrphaNet
#from OrphaNet import RareDiseases
import lxml.etree

#config = {"orpha.net": OrphaNet,
#          "rarediseases": RareDiseases,
#          }

class Crawler(object):
    
    def __init__(self, page, parser=ParserInterface, DbConnection=None):

        # TODO: assert DbConnection instanceOf dbClass
        
        self.page = page
        self.parser = parser(page)


    def __getattr__(self,prop):
        ret = getattr(self.parser, prop)
        #print type(ret())
        if isinstance(ret(), lxml.etree.XPath):
            print "Wee"
            return ret()(self.parser.etree)[0].text
            
        elif isinstance(ret, str):
            print "str"
            # i database
            pass
        print "wtf"

    def case1():
        pass
    
    def case2():
        pass

    def call(n):
        getattr(self, "case" + str(n))()
        
        
        
    
    
