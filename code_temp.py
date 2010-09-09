# Pages to be crawled (by default).
defaultPages=['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Z']

def fetchOprhanetDiseaseURLs(pages=defaultPages):

    """
    Takes a list of letters representing the pages to be crawled for rare
    diseases on http://www.orpha.net.

    Returns a list of URLs linking to describtive pages of the diseases found.

    The default list is:
    ['0','A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','Z']
    """

    diseaseURLs=[]

    # Get a list of rare-disease URLs
    for index in pages:
        page='http://www.orpha.net/consor/cgi-bin/Disease_Search_List.php?lng=EN&TAG=%s' % index

        try:
            c=urllib2.urlopen(page)
        except:
            print "Could not open %s" % page
            continue

        soup=BeautifulSoup(c.read())
        links=soup('a')
        count=0
        for link in links:
            if 'href' in dict(link.attrs):
                if 'OC_Exp.php?lng=EN&Expert' in link['href']:
                    diseaseURLs.append(urljoin(page,link['href']))
                    count+=1

        print index,'completed.',count,'diseases added to list.'

    return diseaseURLs
