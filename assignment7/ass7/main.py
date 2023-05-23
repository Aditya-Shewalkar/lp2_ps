import os
import webapp2
import urllib
import json
from google.appengine.ext.webapp import template
class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),"index.html")
        template_values={}
        self.response.out.write(template.render(path,template_values))

    def post(self):
        dropdown=self.request.get("choices")
        if dropdown=="zip":
            pincode=self.request.get("zipCode")
            url = "https://api.postalpincode.in/pincode/"+pincode

        else:
            query=self.request.get("branchName")
            url = "https://api.postalpincode.in/postoffice/"+branchName
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        status=data[0].['status']
        if status!="success":
            if dropdown=="zip":
                response.out.write("Wrong pincode")
            else:
                response.out.write("wrong areacode")
        else :
            post_office=data[0]['PostOffice'][0]['Name']
            district = data[0]['Postoffice'][0]['District']
            name = data[0]['Postoffice'][0]['Name']
            template_values={
            post_office="post_office"
            name = "name"
            district = "district"
            }

        path = os.path.join(os.path.dirname(__file__),"results.html")
        self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug = True)


