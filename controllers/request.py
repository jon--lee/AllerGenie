import webapp2
import jinja2
import os
import parser


#jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')))
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
peanuts = ["peanut"]
shellfish = ["shellfish"]
wheat = ["wheat"]

base_url = "http://www.yelp.com"

allergyKey = {"peanut": peanuts,
    "shellfish": shellfish,
    "wheat": wheat
    }

class RequestPage(webapp2.RequestHandler):
    def get(self):
        url = base_url + self.request.get('url')
        searchTerm = self.request.get('searchTerm')
        allergy = self.request.get('allergy')
        loc = self.request.get('loc')
        #self.response.out.write(url)
        reviews = parser.parse(url)
        template = jinja.get_template("/request.html")
        template_values = {"searchTerm": searchTerm, "loc": loc, "allergy": allergy}
        self.response.out.write(template.render(template_values))
        
    def post(self):
        self.response.out.write("post request hello world");
        url = self.request.get('url')
        print url
