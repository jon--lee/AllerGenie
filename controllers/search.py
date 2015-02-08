import webapp2
import json

import urllib2

url_base = "http://www.yelp.com/search?"
keyword = 'href="/biz/'
class SearchPage(webapp2.RequestHandler):
    def post(self):
        req = json.loads(self.request.body);
        searchTerm = req['searchTerm']
        loc = req['loc']
        searchTerm = searchTerm.replace(" ", "+")
        loc = loc.replace(" ", "+")


        params = "find_desc=" + searchTerm + "&find_loc=" + loc
        url = url_base + params
        
        

        response = urllib2.urlopen(url)
        htmlString = response.read()
        
        startIndex = 0
        results = []
        endIndex = 0
        for i in range(0, 10):
            startIndex = htmlString.find(keyword, endIndex + 3) + 6
            endIndex = htmlString.find('"', startIndex + 6)
            if (i % 2 == 0):            
                results.append(htmlString[startIndex:endIndex])
        
        
        self.response.out.write(json.dumps(results));
    
    def get(self):
        self.redirect('/')
