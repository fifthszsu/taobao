# -*- coding:UTF-8 -*-
import re
import requests
import os
 
#name=input('input file name')
#robot='C:/Users/Desktop/'+name+'/'
kv={'user-agent':'mozilla/5.0'}
 
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def parserHTML(html):
    pattern="<td><div align=\"center\">\d*.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d*.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d*.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d*.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d*.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d*.?\d*</div></td>"
    reg=re.compile(pattern)
    urls=re.findall(reg,html)
    print(len(urls))
    return urls
 
def download(List):
    for url in List:
        try:
            path=robot+url.split('/')[-1]
            url=url.replace('\\','')
#            print(url)
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            if not os.path.exists(robot):
                os.makedirs(robot)
            if not os.path.exists(path):
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(path+'saved')
            else:
                print('file already exist')
        except:
            continue
 
def getmoreurl(num,word):
    ur=[]
    url=r'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pn}&rn=30'
    for x in range(1,num+1):
        u=url.format(word=word,pn=30*x)
        ur.append(u)
    return ur
    
def main():
#    n=int(input('how many want to down load(n*30)'))
#    word=input('the file name want to download:')
#    url='http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1499773676062_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word={word}'.format(word=word)
#    url='http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/000001.phtml'
    url= 'https://detail.tmall.com/item.htm?id=591050810174&skuId=4053750992099'
    html=getHTMLText(url)
#    urls=parserHTML(html)
    print(html)
#    download(urls)
''' 
    url1=getmoreurl(n,word)
    for i in range(n):
        html1=getHTMLText(url1[i])
        urls1=parserHTML(html1)
        download(urls1)
'''
main()