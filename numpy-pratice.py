import numpy as np
from math import log, sqrt, exp
a = np.linspace(1,20,10)
b = np.logspace(1, 10, num=10, endpoint=True, base=2,dtype=int)
print(a)
print(b)
print("="*30)
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
print(a.T)
b = a[1:3, 1:3]
c = a[1:3,[1,2]]
d = a[...,1:]
print(b)
print(c)
print(d)
print("="*30)
for x in np.nditer(a,order='F'):
    print (x, end=", " )
print ('\n')
print("="*30)
for x in np.nditer(a,order='C'):
    print (x, end=", " )
print ('\n')

#dot multiple
x=np.array([4,5,6,7])
x=np.mat(x)
y=np.array([8,10,12,14])
y=np.mat(y)
k=np.array([5,7,3,10])
k=np.mat(k)
dot1=x*k.T/(sqrt(x[0,0]**2+x[0,1]**2+x[0,2]**2+x[0,3]**2)*sqrt(k[0,0]**2+k[0,1]**2+k[0,2]**2+k[0,3]**2))
dot2=x*y.T/(sqrt(x[0,0]**2+x[0,1]**2+x[0,2]**2+x[0,3]**2)*sqrt(y[0,0]**2+y[0,1]**2+y[0,2]**2+y[0,3]**2))
print(dot1)
print(dot2)