import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stats
import scipy.optimize as opt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
'''
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plot(X,D)
show()


n = 10240
X = np.random.normal(0,3,n)
Y = np.random.normal(0,3,n)
plt.scatter(X,Y)

x = np.arange(-2, 2, .01)
y = np.arange(-2, 2, .01)
x, y = np.meshgrid(x, y)
f = (x*x+y*y-1)**3-x**2*y**3
plt.figure()
plt.contour(x, y, f, 0,)
#plt.title(r'$\left|x\right|+\left|y\right|=1$')
plt.title(r'$(x*x+y*y-1)**3-x**2*y**3=0$')

'''


x1=np.linspace(-np.pi,np.pi,200)
C,S=np.cos(x1),np.sin(x1)
#plt.plot(x1,S)
#plt.plot(x1,C)
x2=[1,0.8,-2,-1,0.01,-1.5]
y2=[0.25,0.5,1,0.01,1,0.2]
#plt.scatter(x2,y2)
plt.title("南新路会所分布图")

x3=np.random.uniform(-0.5,0.5,[1,200])
y3=np.random.random(size=[1,200])
plt.scatter(x3, y3,label="会所")

u = 0   
sig = math.sqrt(0.2)  
print(sig)
x = np.linspace(u - 3*sig, u + 3*sig, 100)
#x = np.linspace(-2,8,50)
y_sig = np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig)
print (x)
print ("="*20)
print (y_sig)
plt.plot(x, y_sig, "r-", linewidth=2)
plt.grid(True)

rv_beta = stats.beta.rvs(size=5, a=4, b=2)
print (rv_beta)
print (np.mean(rv_beta))


plt.show()