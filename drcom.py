#It is coded  for geting Name and Dr.Com ID from Students of NUPT
import re
import urllib.request
from threading import *
import time
class Get_Info(Thread):
    def __init__(self,number,files,line):
        Thread.__init__(self)
        self.Snumber=number
        self.s=files
        self.old_line=line
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
        		self.s.write(self.old_line.split('\n')[0]+"\t"+dr.group()+'\n')
                #self.s.write(dr.group()+'\t'+name.group()+'\t'+self.Snumber+'\n')
sf=open('drcom_num','w')
sd=open('drcom','r')
lines=sd.readlines()
#for line in sd:
#    stu_num=line.split('\t')[0]
#    if int(stu_num[1:3])>6:
#        Get_Info(stu_num,sf,line)
#time.sleep(0.01)
for i in range(7,41):
    for j in range(1000):
        try:
            stu_num=lines[i*1000+j].split('\t')[0]
            print(stu_num+'\n')
            if int(stu_num[1:3])>6:
                Get_Info(stu_num,sf,lines[i*1000+j])
                time.sleep(0.04)
        except Exception as e:
            print(e)
            pass
    time.sleep(50)
sf.close()
