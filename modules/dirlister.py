import os


def ran():
	print "[*] In dirlister module"
	files=os.listdir(".")

	return str(files)
