import os
from os import system
from threading import *
import time

class i_thread(Thread):
	def __init__(self,se):
		Thread.__init__(self)
		self.sec=se
		print("init thread :"+str(self.sec))
		self.start()
	def run(self):
		for i in range(5):
			print(i+self.sec)		
for h in range(10000):
	u_thread=i_thread(h*10)
#	u_thread.run()
