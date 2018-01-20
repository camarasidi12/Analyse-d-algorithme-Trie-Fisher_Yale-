import numpy as np
from scipy import *

t1=np.arange(2)

t2=np.array([2,3])

l1=[1,2,3]
l2=[4,5]


l3=l1.append(l2)
l2[0]=100
print(l1)
print(l3)
print("******************table******************")
t3=append(t1,t2)
t1[0]=111
print(t1)
print(t3)

