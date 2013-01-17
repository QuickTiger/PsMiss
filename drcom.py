#It is used for geting Name and Dr.Com ID from Students of NUPT
import re
import urllib.request
from threading import *
import time
class Get_Info(Thread):
	def __init__(self,number,files):
		Thread.__init__(self)
		self.Snumber=number
		self.s=files
		self.start()
	def run(self):
		url='http://my.njupt.edu.cn/ccs/main/searchUser.do?key='+self.Snumber
		data=urllib.request.urlopen(url)
		info=data.read().decode('utf-8')
		pa1=re.compile(r'(?<=<tr><td>)[\S]{1,10}(?=</td><td>)')
		pa=re.compile(r'[\dA-Z]{10,20}')
		dr=pa.search(info)
		name=pa1.search(info)
		if dr:
			if name:
				print(dr.group()+'\t'+name.group()+'\t'+self.Snumber)
				self.s.write(dr.group()+'\t'+name.group()+'\t'+self.Snumber+'\n')
sf=open('drcom_num','w')
for i in ['08','09','10','11','12']:
	for j in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14']:
		for n in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']:
			for k in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']:
				s='B'+i+j+n+k
				a=Get_Info(s,sf)
				time.sleep(0.2)
			time.sleep(1)
		time.sleep(100)
	time.sleep(200)
sf.close()
