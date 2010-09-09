from Crawler import Crawler
from OrphaNet import OrphaNet

import codecs

import unittest

class TestOrphaNet(unittest.TestCase):

    def setUp(self):
        page = codecs.open("17 ketoreductase deficiency", 'r', 'iso-8859-1')
        #print page
        self.parser = Crawler(page, parser=OrphaNet)
    
    def test_disease_name(self):
        print self.parser.disease_name

    def test_synonyms(self):
        print self.parser.synonyms

    def test_inheritance(self):
        print self.parser.inheritance

    def test_prevalence(self):
        print self.parser.prevalence
    
    def test_summary(self):
        print self.parser.summary

    def test_onset_age(self):
        print self.parser.onset_age

    def test_ICD_10_code(self):
        print self.parser.ICD_10_code

    def test_MIM(self):
        print self.parser.MIM

if __name__ == "__main__":
    unittest.main()

