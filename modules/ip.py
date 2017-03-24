import urllib, json

def ran():
	print "[*] In ip module"
	data= json.loads(urllib.urlopen("http://ip.jsontest.com/").read())


	return str(data["ip"])
