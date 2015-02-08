import urllib2
import re

# @param    url             url to the site that the reviews will be scraped from
# @return   reviewList      list of all the unprocessed reviews on the page(s)
def parse(url):
    response = urllib2.urlopen(url)
    htmlString = response.read()
    startindex = htmlString.find("<p itemprop")

    review_list = []
    count = 0
    while startindex>=0:
        count +=1

        endindex = htmlString.find ("</p>")
        review = htmlString [startindex:endindex]
        review = striphtml (review)

        #print review

        review_list.append(review)

        htmlString = htmlString[endindex+3:]
        startindex = htmlString.find("<p itemprop")
    
    reviews = []
    for review in review_list:
        if not review == "":
            reviews.append(review)
    return reviews


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', data)
