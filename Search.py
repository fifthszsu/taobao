def huiye():
    f = open("E:/Python Project/Resource/Connection.txt", "r")
    str=f.read()
    list = str.splitlines()     #To slice the string by /n
    f.close
    dicConnectPoint={}    # To store information for a single node and the nodes connected to it
    dicFlag={}          # To identify weather the node has been found during the process from original node to target node
    for i in range(0,len(list)):
        dicConnectPoint[i]=[]
        dicFlag[i]=False
    for i in range(0,len(list)):
        print(list[i])
        temList=list[i].split("-")
        print(temList)
        dicConnectPoint[int(temList[0])].append(int(temList[1]))
        dicConnectPoint[int(temList[1])].append(int(temList[0]))
    print (dicConnectPoint)
    print (dicFlag)
    print ("="*30)
#    dfs(dicFlag,dicConnectPoint,0,12)
    bfs(dicFlag,dicConnectPoint,0,12)

def dfs(dicFlag,dicConnectPoint,num,num2):  #deep first search ,can be applied for classify 
    print (str(num)+"-", end = '')
    dicFlag[num]=True
    if dicFlag[num2] == True:
        print ('\n' + "find " + str(num2))
    else:
        for i in dicConnectPoint[num]:
            if dicFlag[i] == False and dicFlag[num2] == False:
                dfs(dicFlag,dicConnectPoint,i,num2)

def bfs(dicFlag,dicConnectPoint,num,num2):   #Breadth-First Search , the idea of first in first out , can be applied to get the minimize path 
    dicEdg={}       # To identify the original node of the edg, e.g dicEDG[4]=0, means from 0 search to 4
    searchList = []
    searchList.append(num)
    strTemp = ''
    while len(searchList) > 0 and dicFlag[num2] ==False:
        dicFlag[searchList[0]]=True
        for i in dicConnectPoint[searchList[0]]:
            if dicFlag[i] == False and dicFlag[num2] == False:
                dicEdg[i]=searchList[0]
                dicFlag[i] = True
                print(i,end = ' ')
                print(dicFlag[i])
                searchList.append(i)    # pop in the next node for search
            elif dicFlag[num2] == True:
                break
        searchList.pop(0)   #The first node is pop out
    x=dicEdg[num2]
    while x!=num:
        strTemp = str(x)+'-'+strTemp 
        x=dicEdg[x]
        print(x)
    print(str(num)+'-'+strTemp)    
    
    
aa=huiye()