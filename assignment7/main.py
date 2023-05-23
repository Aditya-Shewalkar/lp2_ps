import webapp2
import os
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path=os.path.join(os.path.dirname(__file__),"index.html")
        template_values={}
        self.response.out.write(template.render(path,template_values))

    def post(self):
        dropdown=self.request.get("choices")
        if dropdown=="zip":
            pincode=self.request.get("zipCode")
            url = "https://api.postalpincode.in/pincode/"+pincode
        else:
            query=self.request.get("branchName")
            url = "https://api.postalpincode.in/postoffice/"+query
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        status=data[0]['Status']
        if status!="Success":
            if(dropdown=="zip"):
                self.response.out.write("Wrong zip code entered")
            else:
                self.response.out.write("Wrong branch name entered")
        else:
            post_office = data[0]['PostOffice'][0]['State']
            name = data[0]['PostOffice'][0]['Name']
            #block = data[0]['PostOffice'][0]['Block']
            district = data[0]['PostOffice'][0]['District']
            template_values = {
                "post_office": post_office,
                "name": name,
                #"block": block,
                "district": district
            }
            path= os.path.join(os.path.dirname(__file__),"results.html")
            self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)