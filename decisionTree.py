import xlrd
import math
import numpy as np

def main():
    workbook = xlrd.open_workbook(u'E:/Python Project/Resource/decisionTree.xls')
    worksheet= workbook.sheets()[0]
    nrows = worksheet.nrows  
    indexList=[]  
    resultList=[]
    colourList=[]
    rootList=[]
    soundList=[]
    for i in range(nrows):  
        if i == 0: 
            continue
#        print (worksheet.row_values(i)[:5])
        indexList.append(worksheet.row_values(i)[0])
        colourList.append(worksheet.row_values(i)[1])
        rootList.append(worksheet.row_values(i)[2])
        soundList.append(worksheet.row_values(i)[3])
        resultList.append(worksheet.row_values(i)[4])
    Matrix = np.array([indexList,colourList,rootList,soundList,resultList]).T
    print(Matrix)
#    entResult=calculateInfoEntropy(Matrix)
    featureList=[1,2,3]
#    gainColour=calculateGain(Matrix,featureList)
    global nodeList
    nodeList=[]
    global nodeNum
    nodeNum=0
    firstNode='起点'
    generateTree(Matrix,featureList,firstNode)
    for i in nodeList:
        print(str(i.index) + " with name is " + i.name + "; with list is " + str(i.list) + "; with result is " + i.result)
#    print(calculateGain(Matrix,featureList))
    
def calculateInfoEntropy(matrix):
    resultList=list(matrix[:,-1])
    listTemp = list(set(resultList))
    print(listTemp)
    ite = iter(listTemp)
    ent=0
    for x in ite:
        rate=resultList.count(x)/len(resultList)
        ent=ent-rate*math.log(rate,2)
    print (ent)
    return ent

def calculateGain(matrix,featureList):
    entResult=calculateInfoEntropy(matrix)
    entMaxResult=0
    featureIndex=0
    for i in featureList:
        entFeature=entResult
        iv=0
#        print(i)
        dataList=list(matrix[:,i])
        ite = iter(list(set(matrix[:,i])))    
        for x in ite:
            entElement=0
            rateElement=dataList.count(x)/len(dataList)
            iteResult = iter(list(set(matrix[:,-1])))
            for y in iteResult:
                z=matrix[:,i][(matrix[:,i]==x) & (matrix[:,4]==y)]
                rate=len(z)/dataList.count(x)
                if rate!=0:
                    entElement=entElement-rate*math.log(rate,2)
            print(entElement)
            entFeature=entFeature-rateElement*entElement              
            ivRate= dataList.count(x)/len(dataList)
            iv=iv-ivRate*math.log(ivRate,2)

        print ("ent value for column "+str(i)+" is "+str(iv))
        gainRatio=entFeature/iv
        if gainRatio>entMaxResult:
            entMaxResult=gainRatio   
            featureIndex=i 
    print("the best gain ratio index is "+str(featureIndex)+" with value is "+str(gainRatio))     
    return featureIndex

def calculateGainRate(matrix,featureList):
    entResult=calculateInfoEntropy(matrix)
    entMaxResult=0
    featureIndex=0
    for i in featureList:
        entFeature=entResult
#        print(i)
        dataList=list(matrix[:,i])
        ite = iter(list(set(matrix[:,i])))    
        for x in ite:
            entElement=0
            rateElement=dataList.count(x)/len(dataList)
            iteResult = iter(list(set(matrix[:,-1])))
            for y in iteResult:
                z=matrix[:,i][(matrix[:,i]==x) & (matrix[:,4]==y)]
                rate=len(z)/dataList.count(x)
                if rate!=0:
                    entElement=entElement-rate*math.log(rate,2)
            print(entElement)
            entFeature=entFeature-rateElement*entElement    
        if entFeature>entMaxResult:
            entMaxResult=entFeature   
            featureIndex=i 
    print("the best feature index is "+str(featureIndex)+" with value is "+str(entMaxResult))     
    return featureIndex

def generateTree(matrix,featureList,feature):
    global nodeNum
    nodeNum+=1
    global nodeList
    node1=node(nodeNum)
    node1.name=feature
    node1.list=list(matrix[:,0])
    resultList=list(matrix[:,-1])
    if len(set(resultList))==1:     # if the result of that node are all the same
        node1.result=resultList[0]
        nodeList.append(node1)
        return
    elif len(featureList)==0 or featureSameValue(matrix,featureList)==True:     # if all the feature has been used or all the remaining feature value are the same
        iteResult = iter(resultList)
        maxResult=0
        for y in iteResult:
            if resultList.count(y)>maxResult:
                maxResult=resultList.count(y)
                node1.result=y
        nodeList.append(node1)
        return
    nodeList.append(node1)
    bestFeatureIndex=calculateGain(matrix,featureList)
    bestFeatureList=list(matrix[:,bestFeatureIndex])
    iteFeature=list(set(bestFeatureList))
    for x in iteFeature:
        if len(list(matrix[:,bestFeatureIndex][(matrix[:,bestFeatureIndex]==x)]))==0:       #if the domain is already become empty
            nodeNum+=1
            node2=node(nodeNum)
            iteResult = iter(resultList)
            maxResult=0
            for y in iteResult:
                if resultList.count(y)>maxResult:
                    maxResult=resultList.count(y)
                    node2.result=y
            nodeList.append(node2)
            return
        else:
            newMatrix=matrix[(matrix[:,bestFeatureIndex]==x)]
            nextfeatureList=featureList.copy()
            nextfeatureList.remove(bestFeatureIndex)
            print("after remove the list become "+str(nextfeatureList))
            generateTree(newMatrix,nextfeatureList,x)
            
        
        
        
        
        
def featureSameValue(matrix,featureList):
    flag=True
    if len(featureList)>0:
        for i in featureList:
            if len(set(list(matrix[:,i])))!=1:
                flag=False
    return flag


class node:
    def __init__(self,n):
        self.name=''
        self.index=n
        self.result='unknow'
        self.list=[]
main()
    
    