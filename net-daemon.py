#A daemon process to keep network alive in DaHuo NUPT
#!/usr/bin/python
import time
from os import system
while True:
	time.sleep(15)
	system("ping -c 5 202.119.236.20 >/tmp/ping_tmp")
	f=open("/tmp/ping_tmp",'r')
	s=f.read()
	if s.find("0%")==-1:
		system("/etc/init.d/networking restart")
	
	
