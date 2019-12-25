# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from time import sleep
def main():
    chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("disable-web-security")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://login.tmall.com/")
    driver.maximize_window()
    sleep(20)
    csvFileIP = open('E:/Python Project/Resource/taobao.csv','r', newline='')
    reader = csv.reader(csvFileIP)
    csvFile2 = open('E:/Python Project/Resource/prod.csv','a+',newline='',encoding='utf-8-sig')
    writer = csv.writer(csvFile2)
    for link in reader:
        driver.get(link[0])
        idNum=link[0].replace("https://detail.tmall.com/item.htm?id=","")
        print(idNum)
        sleep(2)
        writer.writerow(idNum)
        try:
            getAndprint(driver,writer)
        except:
            print("faile for " + idNum)
            continue
    csvFile2.close()        

def getAndprint(driver,writer):  
#    eleList=driver.find_elements_by_xpath("//dd/ul/li/a/span[text()!='']")
    eleList=driver.find_elements_by_css_selector("div>dl:first-child>dd>ul>li>a>span")
    if len(eleList)==0:
        print("only one product in the link")
    else:
        for j in range(0,len(eleList)):
            try:
                eleList[j].click()
                sleep(1)
        #        ele2=driver.find_element_by_xpath("//dd/span[text()!='']")
                ele3=driver.find_element_by_xpath("//dd/div/span[text()!='']")
                discountPrice=int(float(ele3.text)*0.9)
                print(eleList[j].text + "," + str(discountPrice))      
                dicConnectPoint=[] 
                dicConnectPoint.append(eleList[j].text)
                dicConnectPoint.append(str(discountPrice))
                writer.writerow(dicConnectPoint)
            except:
                continue
main()