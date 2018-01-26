# coding:utf8
from random import randrange
import numpy as np
import time
import sys
sys.setrecursionlimit(150000)



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


def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksortPlace(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksortPlace(myList, start, pivot-1)
        quicksortPlace(myList, pivot+1, end)
    return myList
    
print(quicksortPlace([7,8,9,4,5,6,1,2,3],0,8))


def generator(n):
	""" Fonction de génération des éléments de la liste"""
	L=np.array([],dtype="int")
	for i in range(1,n+1):
		L=np.concatenate( (np.array([i]),L) )
	return L

temps=0
i=1



file=open("inPlace.txt","w") 
while(i<=10000):
    i+=10
    debutPlace=time.time()
    quicksortPlace(sattoloCycle(np.arange(i)),0,i-1)
    finPlace =time.time()
    tempsPlace=finPlace-debutPlace
    
    debutNotPlace=time.time()
    quicksort(sattoloCycle(np.arange(i)))
    finNotPlace =time.time()
    tempsNotPlace=finNotPlace-debutNotPlace
    #print("place "+`tempsPlace`)
    #print("Not place "+`tempsNotPlace`)
    file.writelines(`i`+" "+`tempsPlace`+" "+`tempsNotPlace`+"\n")
file.close();
print(temps/1000)
#print((sattoloCycle(generator(40))))


#file=open("inPlace.txt","w") 
"""while(i<=1000):
    i+=1
    debut=time.time()
    quicksort(sattoloCycle(generator(i)))
    fin =time.time()
    temps=fin-debut
    file.writelines(`i`+" "+`temps`+"\n")
file.close();
print(temps/1000)
#print((sattoloCycle(generator(40))))"""


























