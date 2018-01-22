# coding:utf-8
from arbres import *
from random import randrange

dicFeuil=dict()
def arbreCroissant(l):
	""" On genere un arbre croissant à partir d'une liste trié """
	
	arb=ArbreBinaire(l.pop(0),fils=("#","#"))
	dicFeuil[0]=arb[0]
	dicFeuil[1]=arb[1]
	i=1
	for elm in l:
		r=randrange(len(dicFeuil))
		a=dicFeuil[r]
		i+=1
		newA=ArbreBinaire(i,fils=("#","#"))
		a.racine=elm
		a[0]=ArbreBinaire("#",fils=("#","#"))
		a[1]=ArbreBinaire("#",fils=("#","#"))
		dicFeuil[r]=a[0]
		dicFeuil[i]=a[1]
	return arb	
def azerty():
	
	fg=ArbreBinaire(1,fils=(2,3))
	fd=ArbreBinaire("#")
	arb=ArbreBinaire(1)
	arb[0]=fg
	arb[1]=fd
	a1=arb[0]
	#arb.view()
	a1.racine=100
	a1[0]=ArbreBinaire(77,fils=("#","#"))
	a1[1]=123
	
	#arb.view()
	return arb
#print(arb[1])

azerty()
#arbreCroissant([1,2,3,4,5,6,7,8,9,10]).view()
print(printAbr(arbreCroissant([1,2,3,4,5,6,7,8,9,10])))




