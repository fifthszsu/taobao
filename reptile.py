# -*- coding:UTF-8 -*-
import requests
from contextlib import closing
from bs4 import BeautifulSoup
import re
def download_image_improve():
 
    url = 'http://www.pythonscraping.com/pages/page3.html'
    url2 = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    response.encoding=response.apparent_encoding
    response2 = requests.get(url, stream = True)
    html = response2.text
    print(html)
    bf = BeautifulSoup(html)
    imgs = bf.find_all('img')
    print(imgs)
'''
    targetUrl="http:"+imgs[0].get('src')
#    print(html)
    pattern = re.compile(r'"objURL":"\S+"')   # 查找数字
    result1 = pattern.findall(html)
    print(result1)
    print(result1[0].split('"')[3])
    for i in range(0,len(result1)-1):
        response = requests.get(result1[i].split('"')[3],timeout=10)
        downloadFile = 'E:/Python Project/Resource/pic/huiye'+str(i)+'.jpg'
        with open(downloadFile,'wb') as f:
            f.write(response.content)
            f.close()
            print('save huiye'+str(i))
''' 
if __name__ == '__main__':
    download_image_improve()


    
#aa=getMessage()
    