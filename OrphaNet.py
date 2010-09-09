
from ParserInterface import *

class OrphaNet(ParserInterface):

    def __init__(self, page=None):
        #print page
        if not page is None:
            self.etree = tree(page)
            #print "etree: ", self.etree
        else:
            self.etree = tree("")

    def disease_name(self):
        return xpath("//h1/span")

    def synonyms(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td[2]/table/tbody/tr/td[2]")

    def inheritance(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/ul/li")
                      #/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/ul/li


    def prevalence(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/ul/li")
                      #/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]
    
    def summary(self):
        return xpath("/html/body/div/div[8]/div[3]/div/p")

    def onset_age(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]")
                      #/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]

    def ICD_10_code(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[5]/td[2]/ul/li")

    def MIM(self):
        return xpath("/html/body/div/div[8]/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/ul/li/a")

        
