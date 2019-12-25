# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from time import sleep
import re

def main():
    dicLink={}
    csvFileIP = open('E:/Python Project/Resource/prod.csv','r', newline='',encoding='utf-8-sig')
    readerCSV = csv.reader(csvFileIP)
    
    reader = list()
    for link in readerCSV:
        reader.append(link)    
    print(len(reader))
    keyValue=""
    valueArr=[]
    count=0
    
    for i in range(0,len(reader)):
        if i<len(reader)-1:
            num = re.findall('\d{10}',reader[i][0])
            if len(num)>0:                         
                if count==0:
                    keyValue=reader[i][0]
                elif count>0:
                    if len(valueArr)>0:
                        dicLink[keyValue]=valueArr[:]
                        valueArr.clear()
                    keyValue=reader[i][0]
                count=count+1
            else:
                valueArr.append(reader[i])
        else:
            valueArr.append(reader[i])
            dicLink[keyValue]=valueArr[:]

    chrome_options = Options()
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("disable-web-security")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://login.tmall.com/")
    driver.maximize_window()
    sleep(20)
    ele=driver.find_element_by_xpath("//div/a[@class='zge-info-button']")
    ele.click()
    n = driver.window_handles
    print('handle: ', n)
    driver.switch_to_window(n[-1])
    sleep(3)
    ele3=driver.find_element_by_xpath("//a[@id='bannerButton']")
    ele3.click()
    n = driver.window_handles
    print('handle: ', n)
    driver.switch_to_window(n[-1])
    sleep(5)
#    i=1
    while True: 
        try:
#            print(str(i)+" time")
            ele=driver.find_element_by_css_selector("div.next-overlay-inner>div form>div:nth-child(2)>div>span")
            idNum=ele.text
            print(idNum)
            ele=driver.find_element_by_css_selector("div.next-overlay-inner>div span a")
            ele.click()
            sleep(1)
            ele=driver.find_element_by_css_selector("span>div button")
            ele.click()
            sleep(1)
            eleList=driver.find_elements_by_css_selector("div.next-overlay-inner>div tr td:nth-child(5) input")
            eleList2=driver.find_elements_by_css_selector("div.next-overlay-inner>div tbody>tr.next-table-row>td:nth-child(1)>div")
            for ele in eleList2:
                print(ele.text)
            if len(eleList)==0:
                print("only one product in the link")
            else:
                for i in range(0,len(reader)):
                    if reader[i][0].find(idNum):
                        print(idNum)
                        print(dicLink[idNum])
                        for k in range(0,len(dicLink[idNum])):
                            for j in range(0,len(eleList2)):
                                if dicLink[idNum][k][0]==eleList2[j].text:
                                    eleList[j].send_keys(dicLink[idNum][k][1])
                        break
            flag=True
            while flag:
                sleep(1)
                try:
                    eleList=driver.find_elements_by_css_selector("div.next-overlay-inner>div tr td:nth-child(5) input")
                    if len(eleList)==0:
                        flag=False
                except:
                    sleep(1)        
        except Exception as e:
#            print(e)
            sleep(3)
        i=i+1
        
             
main()
                
        