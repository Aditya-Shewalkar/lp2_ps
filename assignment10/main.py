import os
import webapp2
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path=os.path.join(os.path.dirname(__file__),"index.html")
        template_values={}
        self.response.out.write(template.render(path,template_values))

    def post(self):
        query=self.request.get('query')
        url="http://universities.hipolabs.com/search?name="+query
        data=urllib.urlopen(url).read()
        data=json.loads(data)
        name=data[0]['name']
        country=data[0]['country']
        website=data[0]['web_pages'][0]
        template_values={
            "name" : name,
            "country" : country,
            "website" : website
        }
        path=os.path.join(os.path.dirname(__file__),"results.html")
        self.response.out.write(template.render(path,template_values))

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
