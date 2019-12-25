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
        print("fail to access Sina Finance")
        return 'fail to access Sina Finance'

def parserPrice(html):
    pattern="<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>\s\s\s\s\s<td class=\"tdr\"><div align=\"center\">\d+.?\d*</div></td>"
    reg=re.compile(pattern)
    urls=re.findall(reg,html)
    return urls

def parserDate(html):
    pattern="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php\?symbol=\S*"
    reg=re.compile(pattern)
    urls=re.findall(reg,html)
#    print(len(urls))
    return urls

def getInstrumentList():
    url='https://hq.gucheng.com/gpdmylb.html'
    html=getHTMLText(url)
    pattern="(\d{6})"
    reg=re.compile(pattern)
    stockList=re.findall(reg,html)
    stockList=list(set(stockList))
    stockList.sort()
    print(stockList)
    print(len(stockList))
    return stockList
    
    
def main():
    ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    headers = ['instrument','日期','开盘价','最高价','收盘价','最低价','交易量','交易金额']
    csvFile2 = open('E:\Python Project\Resource\stockList.csv','a+', newline='')
    writer = csv.writer(csvFile2)
#    writer.writerow(headers)
    urlStock='http://money.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/ToBeReplace.phtml' 
    url='http://httpbin.org/get'
    stockList=getInstrumentList()
    print(len(stockList))
    csvFileIP = open('E:\Python Project\Resource\ipList.csv','r', newline='')
    IpAddressHTML=requests.get(url).text
    pattern="(\d+\.\d+\.\d+\.\d+)"
    reg=re.compile(pattern)
    IpAddress=re.findall(reg,IpAddressHTML)
    print("原有IP:   "+IpAddress[0])

    reader = csv.reader(csvFileIP)
    downLoadCount=50
    for IPpair in reader:
        if downLoadCount<100:
            try:
                print(IPpair[0]+" : "+IPpair[1]+"\n")
                proxies={"http":IPpair[0]+":"+IPpair[1]}
                IpAddressHTML=requests.get(url,timeout=5,proxies=proxies).text
                pattern="(\d+\.\d+\.\d+\.\d+)"
                reg=re.compile(pattern)
                IpAddress=re.findall(reg,IpAddressHTML)
                print("new ip" + IpAddress[0])
                IPdownLoadMax=10
                for j in range(downLoadCount,len(stockList)):
                    try:           
                        Flag=True
                        url2=urlStock.replace("ToBeReplace", stockList[j])
                        html=getHTMLText(url2)
                        priceList=parserPrice(html)
                        DateList=parserDate(html)
                        if IPdownLoadMax==0 or "Sina Finance" in html:
                            print("This IP has download 10 stock" + IpAddress[0])
                            print("total download amount is "+str(downLoadCount))
                            Flag=False
                            break      
                        if Flag:
                            for i in range(len(DateList)):
                                pattern="\d+\.?\d*"
                                reg=re.compile(pattern)
                                prices=re.findall(reg,priceList[i])
                                prices.insert(0,DateList[i][-12:-2])
                                prices.insert(0,str(stockList[j]))
                                writer.writerow(prices) 
                            downLoadCount+=1
                            IPdownLoadMax-=1
                    except:
                        print("Ip block, total download amount is "+str(downLoadCount))
                        break                       
            except:
                continue
    ticks2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    csvFile2.close()
    print("Start time "+ ticks +"End time "+ticks2)         
main()