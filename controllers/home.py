


import webapp2
import jinja2
import os



jinja = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../views')))

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja.get_template("/home.html")
        self.response.out.write(template.render());





