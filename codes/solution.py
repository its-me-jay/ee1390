#Author - Jayasimha Reddy

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


p1=np.array([0,2]).T
p2=np.array([-2,4]).T
p21=p2-p1


#c.T*(p2-p1)=(||p2||**2-||p1||**2)/2
#rhs=(||p2||**2-||p1||**2)/2


rhs=(np.linalg.norm(p2)**2-np.linalg.norm(p1)**2)/2

x=(rhs-2*int(p21[1]))/int(p21[0])

c=np.array([x,2]).T

r=int(np.linalg.norm(c-p1))
x=np.linspace(c[0]-r,c[0]+r,1000)

def circle(c,r):
    X=[]
    Y=[]
    for i in range(len(x)):
        k=(r**2-(x[i]-c[0])**2)**0.5
        X.append(x[i])
        Y.append(k+c[1])
        X.append(x[i])
        Y.append(-k+c[1])
    return X,Y

circle_x,circle_y=circle(c,r)
plt.scatter(circle_x,circle_y)     #Plot corresponding to circle
plt.scatter(c[0],c[1])

#Substitute the center in the options given to check if any of them represents a diameter

res=np.matmul(np.matrix([4,5]),c)-6
if(int(res)==0):
    print("Answer is option a")

res=np.matmul(np.matrix([2,-3]),c)+10
if(int(res)==0):
    print("Answer is option b")

res=np.matmul(np.matrix([3,4]),c)-3
if(int(res)==0):
    print("Answer is option c")

res=np.matmul(np.matrix([5,2]),c)+4
if(int(res)==0):
    print("Answer is option d")

y=[]
for i in range(len(x)):
    y.append((6-4*x[i])/5)                   #Line segment corresponding to option a
plt.plot(x,y,label="option a")

y=[]
for i in range(len(x)):
    y.append((-10-2*x[i])/-3)                #Line segment corresponding to option b
plt.plot(x,y,label="option b")

y=[]
for i in range(len(x)):
    y.append((3-3*x[i])/4)                   #Line segment corresponding to option c
plt.plot(x,y,label="option c")

y=[]
for i in range(len(x)):
    y.append((-4-5*x[i])/2)
plt.plot(x,y,label="option d")               #Line segment corresponding to option d
plt.title("Option b is the answer")
plt.legend()
plt.show()
