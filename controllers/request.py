import webapp2
import jinja2
import os
import parser
import processor

#jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')))
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
peanuts = ["peanut"]
shellfish = ["shellfish", "crab", "lobster", "prawns", "shrimp"]
wheat = ["wheat", "bread", "cereal", "pasta"]
eggs = [" egg", "omelet"]

base_url = "http://www.yelp.com"

allergyKey = {"peanut": peanuts,
    "shellfish": shellfish,
    "wheat": wheat,
    "eggs": eggs
    }

class RequestPage(webapp2.RequestHandler):
    def get(self):
        url = base_url + self.request.get('url')
        searchTerm = self.request.get('searchTerm')
        allergy = self.request.get('allergy')
        loc = self.request.get('loc')
        #self.response.out.write(url)
        reviews = parser.parseMultiplePages(url, 39)
        #reviews = ["more text here. hello some peanut. and another peanut over here", "none here do nothing.", "nothing here as well."]
        phrases = processor.process(reviews, allergyKey[allergy])
        template = jinja.get_template("/request.html")
        response = "Inconclusive"
        if(len(phrases) == 0):
            response = "This place looks safe. We did not find any indicators related to your allergy."
        if(len(phrases) > 0):
            response = "We found a few indicators related to your allergy."
        if(len(phrases) > 3):
            response = "Maybe you should avoid this place.\nWe found several indicators related to your allergy."
        if(len(phrases) > 15):
            response = "You should probably avoid this place.\nWe found MANY indicators related to your allergy."
        template_values = {"searchTerm": searchTerm, "loc": loc, "allergy": allergy, "phrases": phrases, "response": response}
        self.response.out.write(template.render(template_values).encode('utf-8'))
        
    def post(self):
        self.response.out.write("post request hello world");
        url = self.request.get('url')
        print url
