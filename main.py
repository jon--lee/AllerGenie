import webapp2
from controllers import home
from controllers import request
app = webapp2.WSGIApplication([
    ('/', home.HomePage),
    ('/request/', request.RequestPage),
    ],debug=True)
