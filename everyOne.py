def theDaysNeedToCoverAll (num):
    totalNum = num
    x=1
    z=0
    while num>0:
        y = num/totalNum
        x = (1+y*x)/y      
        z=z+totalNum/num
        num = num -1       
    print (x)
    print (z)
    
aa=theDaysNeedToCoverAll(3000)