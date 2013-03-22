#This is intended to get your photo from the coming graduation certificate in Universities of Jiangsu Province. It need your StudentID and IDcard number
import urllib,urllib2
import re


# Information Configure
StudentID=''
IDcard=''
fdir=''
# End Configure
def login(StudentID,IDcard):
	posturl='http://www.91job.gov.cn/student/default.aspx'
	postdata='__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTEyOTUxNDUzNzkPZBYCAgEPZBYEAgMPEA8WAh4HQ2hlY2tlZGdkZGRkAgcPEA8WAh8AaGRkZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFDFJhZGlvQnV0dG9uMQUMUmFkaW9CdXR0b24yBQxSYWRpb0J1dHRvbjLnYmSPeph%2FtcYq%2FSbhCyGotMaKFA%3D%3D&RadioButton1=RadioButton1&xhTextBox='+StudentID+'&xmTextBox=&sfzTextBox='+IDcard+'&Button1=%E7%A1%AE+%E5%AE%9A'
	headers={'Host' : 'www.91job.gov.cn','Origin' : 'http://www.91job.gov.cn','Referer' : 'http://www.91job.gov.cn/student/default.aspx','User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.27 (KHTML, like Gecko) Chrome/26.0.1386.0 Safari/537.27'}
	request=urllib2.Request(posturl,postdata,headers)
	response=urllib2.urlopen(request)
	t=response.read()
	id_pa=re.compile(r'(?<=result.aspx\?cid=)[A-Z0-9]+')
	ID=id_pa.search(t).group(0)
	return(ID)
def getdata(StudentID,ID, fdir):
	img=urllib2.urlopen('http://www.91job.gov.cn/student/readimg.aspx?id='+ID)
	f=open(fdir+'/'+StudentID+'.jpg','w')
	f.write(img.read())
	f.close()

getdata(StudentID,login(StudentID,IDcard),fdir)
