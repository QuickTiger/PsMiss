import os 
from threading import *
class a(Thread):
	def __init__(self,f):
		Thread.__init__(self)
		self.fi=f
		self.start()
	def run(self):
		print(self.fi.readline())
f=open('/root/123','r')
for i in range(1000):
	xx=a(f)

