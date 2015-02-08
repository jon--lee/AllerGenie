import webapp2
import json

import urllib2
import re
url_base = "http://www.yelp.com/search?"
#url_base = "http://www.yelp.com/search"
keyword = 'href="/biz/'

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


class SearchPage(webapp2.RequestHandler):
    def post(self):
        req = json.loads(self.request.body);
        searchTerm = req['searchTerm']
        loc = req['loc']
        searchTerm = searchTerm.replace(" ", "+")
        loc = loc.replace(" ", "+")


        params = "find_desc=" + searchTerm + "&find_loc=" + loc
        url = url_base + params
        
               
        opener = urllib2.build_opener()
        opener.addHeaders = [('User-agent', 'Mozilla/5.0')]
        response = opener.open(url)

        #response = urllib2.urlopen(url)
        htmlString = response.read()
        
        startIndex = 0
        results = []
        endIndex = 0
        for i in range(0, 10):
            startIndex = htmlString.find(keyword, endIndex + 3) + 6
            endIndex = htmlString.find('"', startIndex + 6)
            if (i % 2 == 1):            
                link = htmlString[startIndex:endIndex]
                si = htmlString.find(">", endIndex + 2)  + 1
                ei = htmlString.find("</a>", si)
                name = striphtml(htmlString[si:ei])
                print name
                tup = (name, link)
                #results.append(htmlString[startIndex:endIndex])
                results.append(tup)
        
        self.response.out.write(json.dumps(results));
    
    def get(self):
        self.redirect('/')
