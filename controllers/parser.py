import urllib2

def parse(url):
    response = urllib2.urlopen(url)
    htmlString = response.read()
