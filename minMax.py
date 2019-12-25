'''
chess game
the first player(odd row) try to get the biggest number
while the second player(even row) try to get the smallest number
when the final score(last row) is known, what is the best result the first player can get  
below tree is a simple mode for each step , both player can only have two choice
'''

import random
def buildTree(deepth,breadth):
    treeWild=breadth**deepth
    print(treeWild)
    cumulateNum = 0  
    dicChild={}
    global dicValue
    dicValue={}
    global dicRowNum
    dicRowNum={}
    global nodeList
    nodeList=[]
    for i in range(1,deepth+1):
        tempList=[]
        rowNum = 2**(i-1)
        cutNum = treeWild//(rowNum+1)
        while rowNum>0:
            cumulateNum+=1
            if i!=deepth:
                dicChild[cumulateNum]=[cumulateNum*2,cumulateNum*2+1]
                dicValue[cumulateNum]=-1
            else:
                dicValue[cumulateNum]=random.randint(1,20)
            dicRowNum[cumulateNum]=i
            print("  "*cutNum,end='')
            print(cumulateNum,end='')
            rowNum-=1
            tempList.append(cumulateNum)
        print(" ")
        nodeList=tempList+nodeList
    print("="*40)
    print(nodeList)
    global maxNum
    maxNum=max(nodeList)
    print("="*40)   
    print(dicValue)
    global _countNum
    global disTempValue
    disTempValue={}
    _countNum=0
    print("the best result it can get is " + str(minMax(dicChild,dicValue,dicRowNum,1)))
    print("it has run recursive for "+str(_countNum)+" times")
    cumulateNum2 = 0 
    for i in range(1,deepth+1):
        rowNum = 2**(i-1)
        cutNum = treeWild//(rowNum+1)
        while rowNum>0:
            cumulateNum2+=1
            print("  "*cutNum,end='')
            print(dicValue[cumulateNum2],end='')
            rowNum-=1
        print(" ")
    for i in range(1,treeWild//2):
        dicValue[i]=-1
    _countNum=0
    print(dicValue)
    print("="*40)
#    print("the best result it can get is " + str(minMaxAB(dicChild,dicValue,dicRowNum,1)))
    print("the best result it can get is " + str(minMaxABF(dicChild,dicValue,dicRowNum)))
    print("it has run recursive for "+str(_countNum)+" times")
    cumulateNum2 = 0 
    for i in range(1,deepth+1):
        rowNum = 2**(i-1)
        cutNum = treeWild//(rowNum+1)
        while rowNum>0:
            cumulateNum2+=1
            print("  "*cutNum,end='')
            print(dicValue[cumulateNum2],end='')
            rowNum-=1
        print(" ")
'''
below algo need to calculate all the values for each steps, the countNum will always be 7 no matter the score is in the last row
'''    
def minMax(dicStructure,dicValue,dicRowNum,startNum):
    global _countNum
    _countNum+=1
    if dicRowNum[startNum]%2==1:
        if dicValue[startNum*2]>0 and dicValue[startNum*2+1]>0:
            dicValue[startNum]=max(dicValue[startNum*2],dicValue[startNum*2+1])
        else:
            dicValue[startNum]=max(minMax(dicStructure,dicValue,dicRowNum,startNum*2),minMax(dicStructure,dicValue,dicRowNum,startNum*2+1))
    else:
        if dicValue[startNum*2]>0 and dicValue[startNum*2+1]>0:
            dicValue[startNum]=min(dicValue[startNum*2],dicValue[startNum*2+1])
        else:
            dicValue[startNum]=min(minMax(dicStructure,dicValue,dicRowNum,startNum*2),minMax(dicStructure,dicValue,dicRowNum,startNum*2+1))
    return dicValue[startNum]

def abandon(num):
    global nodeList
    global maxNum
#    print(str(maxNum)+ " drop number "+str(num))
    if 2*num not in nodeList and 2*num+1 not in nodeList:
        if num in nodeList:
            nodeList.remove(num)
    else:
        abandon(2*num)
        abandon(2*num+1)
        if num in nodeList:
            nodeList.remove(num)

def calculateValue(num):
    global nodeList
    global dicValue
    global dicRowNum
    global disTempValue
    if num*2 not in nodeList and dicValue[num*2+1]>0:
        dicValue[num]=dicValue[num*2+1]
    elif num*2+1 not in nodeList and dicValue[num*2]>0:
        dicValue[num]=dicValue[num*2]
    elif dicValue[num*2]>0 and dicValue[num*2+1]>0:
        if dicRowNum[num]%2==1:
            dicValue[num]=max(dicValue[num*2],dicValue[num*2+1])
        else:
            dicValue[num]=min(dicValue[num*2],dicValue[num*2+1])

def abAlgo(firstNode):
    global nodeList
    global dicValue
    global dicRowNum
    global disTempValue
    childNode=firstNode*2
    conflitFlag=False   #If Flag=ture, means the node need to be abandoned
    if dicRowNum[firstNode]%2==1:   #Odd row
            while childNode//4>0:
                if childNode//4 in disTempValue and disTempValue[firstNode]>disTempValue[childNode//4]:
                    conflitFlag=True
                    if firstNode>=4:
                        if firstNode//4 in disTempValue and disTempValue[firstNode//4]<disTempValue[childNode//4]:
                            conflitFlag=False
                childNode=childNode//4
    else:   #Even row
            while childNode//4>0:
                if childNode//4 in disTempValue and disTempValue[firstNode]<disTempValue[childNode//4]:
                    conflitFlag=True
                    if firstNode>=4:
                        if firstNode//4 in disTempValue and disTempValue[firstNode//4]>disTempValue[childNode//4]:
                            conflitFlag=False
                childNode=childNode//4
#    print(str(firstNode)+ " the flag is " + str(conflitFlag))
    if conflitFlag==True:   #abandon firtNode case
        if firstNode%2==1 and dicRowNum[firstNode]>1:
            if firstNode-1 not in nodeList:
#                print("into first")
                abandon(firstNode//2)
            else:
#                print("into second")
                dicValue[firstNode//2]=dicValue[firstNode-1]
                abandon(firstNode)
                if firstNode//4 not in disTempValue:
                    disTempValue[firstNode//4]=dicValue[firstNode-1] 
                    abAlgo(firstNode//4)
        elif firstNode%2==0 and dicRowNum[firstNode]>1:
            abandon(firstNode)
    else:   #not abandon firstNode, then need to calculate its value
        calculateValue(firstNode)
#        print("cal result of "+str(firstNode) + " is "+str(dicValue[firstNode]))
        if firstNode>1:
            if firstNode%2==0:
                if firstNode//2 not in disTempValue and dicValue[firstNode]>0:
                    disTempValue[firstNode//2]=dicValue[firstNode]
#                    print (disTempValue)
#                    print (str(firstNode//2)+" value is " + str(dicValue[firstNode//2]))
                    abAlgo(firstNode//2)
            else:
                calculateValue(firstNode//2)
                if firstNode>=4:
                    if firstNode//4 not in disTempValue and dicValue[firstNode//2]>0:
                        disTempValue[firstNode//4]=dicValue[firstNode//2]
                        abAlgo(firstNode//4)
    
        
def minMaxABF(dicStructure,dicValue,dicRowNum):
    global _countNum
    global nodeList
    copyList=nodeList.copy()
    global disTempValue
    print(nodeList)
    for i in range(0,len(copyList)):
        if  copyList[i] in nodeList and dicValue[copyList[i]]<0:
#            print("main function go to "+str(copyList[i]))
            _countNum+=1
#            print("-"*50)
#            print(nodeList)
#            print(disTempValue)
            firstNode=copyList[i]
            if firstNode not in disTempValue:
                print(str(firstNode)+" into algo")
                disTempValue[firstNode]=dicValue[firstNode*2]
                abAlgo(firstNode)
            else:
                calculateValue(firstNode)
    return dicValue[1]   
 
 
            
  
def minMaxAB(dicStructure,dicValue,dicRowNum,startNum):
    global _countNum
    global nodeList
    copyList=nodeList.copy()
    global disTempValue
    print(nodeList)
    for i in range(0,len(copyList)):
        if  copyList[i] in nodeList and dicValue[copyList[i]]<0:
            _countNum+=1
#            print("-"*50)
#            print(nodeList)
#            print(disTempValue)
            firstNode=copyList[i]
#            print(firstNode)
            conflitFlag=False
            childNode=firstNode*2
            disTempValue[firstNode]=dicValue[firstNode*2]
            if dicRowNum[firstNode]%2==1:   #Odd row
                while childNode//4>0:
                    if childNode//4 in disTempValue and disTempValue[firstNode]>disTempValue[childNode//4]:
                        abandon(firstNode)
#                        print("*"*30)
#                        print(nodeList)
                        if firstNode%2==1:
                            dicValue[firstNode//2]=dicValue[firstNode-1]
                            if firstNode//4 not in disTempValue:
                                disTempValue[firstNode//4]=dicValue[firstNode-1]
                            abandon(firstNode//2)
                        conflitFlag=True
                        break
                    childNode=childNode//4
                if conflitFlag==False:
                    dicValue[firstNode]=max(dicValue[firstNode*2],dicValue[firstNode*2+1])
                    abandon(firstNode)
                    if firstNode%2==0:
                        disTempValue[firstNode//2]=dicValue[firstNode]
                    else:
                        dicValue[firstNode//2]=min(dicValue[firstNode-1],dicValue[firstNode])
                        if firstNode//4 not in disTempValue:
                            disTempValue[firstNode//4]=dicValue[firstNode//2]
                        abandon(firstNode//2)
#                        print("=-"*30)
#                        print(nodeList)
            else:   #Even row
                while childNode//4>0:
                    if childNode//4 in disTempValue and disTempValue[firstNode]<disTempValue[childNode//4]:
                        abandon(copyList[i])
#                        print("*"*30)
#                        print(nodeList)
                        if firstNode%2==1:
                            dicValue[firstNode//2]=dicValue[firstNode-1]
                            if firstNode//4 not in disTempValue:
                                disTempValue[firstNode//4]=dicValue[firstNode-1]
                            abandon(firstNode//2)
                        conflitFlag=True
                        break
                    childNode=childNode//4
                if conflitFlag==False:
                    dicValue[firstNode]=min(dicValue[firstNode*2],dicValue[firstNode*2+1])
                    abandon(firstNode)
                    if firstNode%2==0:
                        disTempValue[firstNode//2]=dicValue[firstNode]
                    else:
                        dicValue[firstNode//2]=max(dicValue[firstNode-1],dicValue[firstNode])
                        if firstNode//4 not in disTempValue:
                            disTempValue[firstNode//4]=dicValue[firstNode//2]
                        abandon(firstNode//2)
#                        print("=-"*30)
#                        print(nodeList)      
    return dicValue[1]  
aa=buildTree(5,2)