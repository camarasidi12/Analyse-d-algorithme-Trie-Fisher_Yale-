# coding:utf8
from random import randrange
import time




def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
	return items

def quicksort (L):
	""" list[int] −> list[int] """
	if len(L) <= 1:
		return L[:]
			
	pivot = L[0]
	R = [pivot]
	p = 0
		
	for i in range(1,len(L)):
		if L[i] < pivot:
			R = R[:p] + [L[i]] + R[p:]
			p = p+1
		else:
			R = R + [L[i]]
	return quicksort (R[:p]) + [R[p]] + quicksort (R[p+1:])


def generator(n):
	""" Fonction de génération des éléments de la liste"""
	L=[]
	for i in range(1,n+1):
		L+=[i]
	return L	
	
debut=time.time()
quicksort(sattoloCycle(generator(1000)))

fin =time.time()
print(fin-debut)





