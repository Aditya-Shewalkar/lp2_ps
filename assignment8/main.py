import webapp2
import os
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path=os.path.join(os.path.dirname(__file__),'index.html')
        template_values={}
        self.response.write(template.render(path,template_values))
    def post(self):
        lat=self.request.get('lat')
        lon=self.request.get('lon')
        url= "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+lon+"&hourly=temperature_2m"
        data=urllib.urlopen(url).read()
        data=json.loads(data)
        timezone=data['timezone']
        temperature=data['hourly']['temperature_2m'][0]
        path=os.path.join(os.path.dirname(__file__),'results.html')
        template_values={
            'timezone' : timezone,
            'temperature' : temperature
        }
        self.response.write(template.render(path,template_values))

app=webapp2.WSGIApplication([('/',MainPage)],debug=True)