import requests


class Echo():
    def doit(self, value):
        #print "Hello World"
        return value

    def do_request(self):
        r = requests.get("http://demo.jmbo.org/api/v1/listing/1/?format=json")
        return r.json
