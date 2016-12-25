import urllib, json

data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
print data["ip"]
