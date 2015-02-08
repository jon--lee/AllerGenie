import webapp2

class HomePage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("hello world");
