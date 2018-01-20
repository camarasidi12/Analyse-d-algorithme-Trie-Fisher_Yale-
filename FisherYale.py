# coding:utf8
from random import randrange
import numpy as np
import time




def sattoloCycle(items):
    i = len(items)
    k=[]
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        #k+=[j]
        print(j)
        items[j], items[i] = items[i], items[j]
	return items

def quicksort (L):
	""" list[int] −> list[int] """
	if len(L) <= 1:
		return L[:]
			
	pivot = L[0]
	R = np.array([pivot])
	p = 0
		
	for i in range(1,len(L)):
		if L[i] < pivot:
			R = np.concatenate((np.concatenate((R[:p],[L[i]])),R[p:]))
			p = p+1
		else:
			R = np.concatenate( (R, np.array([L[i]]) ) )
	return np.concatenate(( np.concatenate( (quicksort(R[:p]),[R[p]]) ),quicksort(R[p+1:]) ))


def generator(n):
	""" Fonction de génération des éléments de la liste"""
	L=np.array([],dtype="int")
	for i in range(1,n+1):
		L=np.concatenate( (np.array([i]),L) )
	return L

temps=0
i=1000
while(i>0):
    i-=1
    debut=time.time()
    quicksort(sattoloCycle(generator(650)))
    fin =time.time()
    temps+=fin-debut
print(temps/1000)
#print((sattoloCycle(generator(40))))


























