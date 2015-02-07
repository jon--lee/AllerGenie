import webapp2
app = webapp2.WSGIApplication([
    ('/', home.HomePage),
    ('/request/', home.HomePage),
    ],debug=True)
