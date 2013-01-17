#In NUPT's Local Network ,The ip of Gateway is always assigned to xx.xx.xx.20
#So,this script can find all the subnetwork of class C in NUPT by ping the assigned Gateway
from os import system
from threading import *
class gatesca(Thread):
	def __init__(self,ip):
		Thread.__init__(self)
		self.ip=ip
		self.start()
	def run(self):
		system("ping -c 5 "+self.ip+" >/tmp/"+self.ip)
		self.f=open("/tmp/"+self.ip,'r')
		self.re=0
		for line in self.f:
			if line.find("100%")!=-1:
				self.re=1
		self.f.close()
		if self.re==0:
			self.fil=open('/root/ping_scan_result','a')
			self.fil.write(self.ip+"\n")
			self.fil.close()
		system("rm /tmp/"+self.ip)

thread_list=[]
for i in range(1,255):
	for j in range(1,255):
		thread_list.append(gatesca("10."+str(j)+"."+str(i)+".20"))
	
