# -*- coding:UTF-8 -*-
import re
import requests
import time
import csv

kv={'user-agent':'mozilla/5.0'}

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def parserPrice(html):
    pattern="<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>"
    reg=re.compile(pattern)
    urls=re.findall(reg,html)
#    print(len(urls))
    return urls

def parserDate(html):
    pattern="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php\?symbol=\S*"
    reg=re.compile(pattern)
    urls=re.findall(reg,html)
#    print(len(urls))
    return urls

def getTime():
    url0='https://www.xicidaili.com/wt/'
    stockListAll=[]
    for i in range(2,30):
        url=url0+str(i)
        print(url)
        html=getHTMLText(url)
        pattern="(<td>(\d+分钟|\d+小时|\d+天)</td>)"
        reg=re.compile(pattern)
        stockList=re.findall(reg,html)
#        print("the length of suivice match is " + str(len(stockList)))
#        print(stockList)
        stockListAll.extend(stockList)    
    return stockListAll

def getPort():
    url0='https://www.xicidaili.com/wt/'
    stockListAll=[]
    for i in range(2,30):
        url=url0+str(i)
        print(url)
        html=getHTMLText(url)
        pattern="(<td>\d+\.\d+\.\d+\.\d+</td>\s\s\s\s\s\s\s<td>\d*</td>)"
        reg=re.compile(pattern)
        stockList=re.findall(reg,html)
#        print("the length of port match is " + str(len(stockList)))
#        print(stockList)
        stockListAll.extend(stockList)    
    return stockListAll
    
    
def main():
    ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#    headers = ['IP','Port']
    csvFile2 = open('E:\Python Project\Resource\ipList.csv','a+', newline='')
    writer = csv.writer(csvFile2)
#    writer.writerow(headers)
    portList=getPort()
    timeList=getTime()
    for j in range(len(portList)):
        if timeList[j][0].find("小时") or timeList[j][0].find("天"):
            pattern="(\d+\.\d+\.\d+\.\d+)"
            reg=re.compile(pattern)
            ips=re.findall(reg,portList[j])
            print("begin list "+portList[j])
            portList[j] = re.sub(r'\d+\.\d+\.\d+\.\d+', "", portList[j])
            print("remain list "+portList[j])
            pattern="(\d+)"
            reg=re.compile(pattern)
            ports=re.findall(reg,portList[j])
            prices=[ips[0],ports[0],timeList[j][1]]
            print(prices)
            writer.writerow(prices) 
    ticks2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    csvFile2.close()
    print("Start time "+ ticks +"End time "+ticks2)
           
main()