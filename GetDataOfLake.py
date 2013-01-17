#A simple scripts of Download data from TaiHu Lake
import re
import urllib.request
f=open('data.txt','w')
for i in range(60617-54291):
    n=i+54291
    print(n)
    data_url="http://www.lakesci.csdb.cn/page/showItem.vpage?id=lakesci.csdb.cn.rgjc.zdhpszzdjc/"+str(n)
    s=urllib.request.urlopen(data_url)
    data=s.read().decode('utf-8')
    pattern=re.compile(r'(?<=6px;\" >﻿)[\d.]+')
    #print(data)
    #print(pattern.search(data).group())
    mm=pattern.findall(data)
    for item in mm:
        f.write(item+'\t')
    f.write('\n')
f.close()
