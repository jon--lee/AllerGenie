import webapp2
from controllers import home
from controllers import request
from controllers import search
app = webapp2.WSGIApplication([
    ('/', home.HomePage),
    ('/request/', request.RequestPage),
    ('/search/', search.SearchPage),
    ],debug=True)
