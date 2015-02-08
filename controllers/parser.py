import urllib2

# @param    url             url to the site that the reviews will be scraped from
# @return   reviewList      list of all the unprocessed reviews on the page(s)
def parse(url):
    response = urllib2.urlopen(url)
    htmlString = response.read()

    
