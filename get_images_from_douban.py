import urllib2,urllib,re,os

'''
http://www.dbmeizi.com/category/2?p=%
'''

def get_url_from_douban():
    url_list=[]
    p=re.compile(r'''<img.*?src="(.+?\.jpg)''') 
    for i in range(1,50):
        target = r"http://www.dbmeizi.com/category/2?p=%d"%i
        req=urllib2.urlopen(target)
        result=req.read()
        matchs=p.findall(result)
        url_list.extend(matchs)
    return url_list

def download_pic(url_list):
    count=0
    if not os.path.exists('/tmp/pic'):
        os.mkdir('/tmp/pic/')
    for url in url_list:
        urllib.urlretrieve(url,'/tmp/pic/'+str(count)+'.jpg')
        count+=1


if __name__=='__main__':
    print "start getting url..."
    url_lists=get_url_from_douban()
    print "url getted! downloading..."
    download_pic(url_lists)
    print "download finish!!!"

