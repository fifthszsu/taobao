class node:
    def __init__(self,n):
        self.name=n
        self.connectNode=[]
        self.colour=''
        self.father=node
        self.domain=['Red','Green','Yellow']
#        self.domain=['Red','Green','Yellow','Blue']

def getStructure():
    f = open("E:/Python Project/Resource/color.txt", "r")
    str=f.read()
    list = str.splitlines()     #To slice the string by /n
    f.close
    dicConnectPoint={}    # To store information for a single node and the nodes connected to it
    for i in range(0,len(list)):
        temList=list[i].split("-")
#        print(temList)
        if temList[0] not in dicConnectPoint:
            dicConnectPoint[temList[0]]=[]
        if temList[1] not in dicConnectPoint:
            dicConnectPoint[temList[1]]=[]
        dicConnectPoint[temList[0]].append(temList[1])
        dicConnectPoint[temList[1]].append(temList[0])
    return dicConnectPoint

def fillColor(node):
    print("filling colour for "+node.name)
    neighborColorList=[]
    for x in node.connectNode:
        print (node.name + " checking the color of subnode "+x.name)
        if not x.colour=='' and x.colour not in neighborColorList:
            neighborColorList.append(x.colour)
    print (neighborColorList)
    node.domain = [i for i in node.domain if i not in neighborColorList]
    print (node.name + " can pick up color as "+str(node.domain))
    node.colour=node.domain[0]
    print (node.name + " picking up color as " +node.colour)
    
def dfs(starNode):  #deep first search ,can be applied for classify 
    global countNum
    countNum=countNum+1
    global beginNodeName
    if starNode.colour =='':
        print("filling colour for "+starNode.name)
        neighborColorList=[]
        for x in starNode.connectNode:
            print (starNode.name + " checking the color of subnode "+x.name)
            if not x.colour=='' and x.colour not in neighborColorList:
                neighborColorList.append(x.colour)
        print (neighborColorList)
        starNode.domain = [i for i in starNode.domain if i not in neighborColorList]
        print (starNode.name + " can pick up color as "+str(starNode.domain))
        if starNode.domain:
            starNode.colour=starNode.domain[0]
        else:
            if starNode.name==beginNodeName:
                print("dead end!!!")
                exit("good game")
            print("try to go upper level")
            starNode.domain=['Red','Green','Yellow']     #restore to father level
            starNode.father.colour=''
            starNode.father.domain.pop(0)
            dfs(starNode.father)
        print (starNode.name + " picking up color as " +starNode.colour)
    for i in starNode.connectNode:
        if i.colour =='':
            i.father=starNode
            print("it comes from "+i.father.name+ " to "+i.name)
            dfs(i)

'''            
            if starNode.name==beginNodeName:
                print("dead end!!!")
                return
            else:
'''


def generateNode(Strlist):  
    nodeList=[]
    dicName={}
    for x in Strlist:
        dicName[x]=node(x)
        nodeList.append(dicName[x])
    for y in nodeList:
        for i in range(0,len(Strlist[y.name])):
#            sunNode=node(Strlist[y.name][i])      
            y.connectNode.append(dicName[Strlist[y.name][i]])
    return nodeList
   
def main():
    Strlist=getStructure()
    nodeList=generateNode(Strlist)
    for i in range(0,len(nodeList)):
        print("number "+str(i) +" for " + nodeList[i].name)
    n=int(input('from which number you want to start with (begin from0)  :  '))
    global beginNodeName
    beginNodeName=nodeList[n].name
    global countNum
    countNum=0
    dfs(nodeList[n])
    for x in nodeList:
        print(x.name + " has color as " +x.colour)
    print("it has run times: " + str(countNum))
main()