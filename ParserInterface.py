from lxml import etree as _etree

def xpath(path):
    #print "blah"
    a =  _etree.XPath(path)
    #print type(a)
    return a

def tree(page):
    parser = _etree.HTMLParser()
    return _etree.parse(page, parser)
    
    

class ParserInterface(object):

    properties = {}

    def disease_name(self):
        raise NotImplemented

    def synomyms(self):
        raise NotImplemented

    def summary(self):
        raise NotImplemented

    def prevalence(self):
        raise NotImplemented
    
    def onset_age(self):
        raise NotImplemented

    def inheritance(self):
        raise NotImplemented

    def ICD_10_code(self):
        raise NotImplemented

    def MIM(self):
        raise NotImplemented

    
