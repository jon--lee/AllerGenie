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


        review_list.append (review)

        htmlString = htmlString[endindex+3:]
        startindex = htmlString.find("<p itemprop")

    return review_list

#review_maxlimit is the maximum number of reviews you want to parse through
def parseMultiplePages (url, review_maxlimit):
    addon = "?start="
    #updates by intervals of 40 which corresponds to the number of reviews per page
    reviewcount = 0

    #total number of reviews parse
    reviews_parsed =0
    review_list = []

    while reviewcount <= review_maxlimit:
        response = urllib2.urlopen(url + addon +str(reviewcount))
        htmlString = response.read()
        startindex = htmlString.find("<p itemprop")

        reviewcount += 40
        #40 is the number of reviews per page
        if startindex < 0:
            break


        while startindex>=0 and reviews_parsed <review_maxlimit:

            endindex = htmlString.find ("</p>")
            review = htmlString [startindex:endindex]
            review = striphtml (review)

            #print review
            if not len(review)==0:
                reviews_parsed +=1
                review_list.append (review)

            htmlString = htmlString[endindex+3:]
            startindex = htmlString.find("<p itemprop")

    #print "Reviews Parsed: " + str(reviews_parsed)
    return review_list

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub(' ', data)


#parseMultiplePages ("http://www.yelp.com/biz/tpumps-cupertino", 400)
