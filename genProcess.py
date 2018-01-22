#coding:utf-8
from random import randrange


def generator(n):
    """ la fonction permettant la generation d'un graphe de taille passer en paramettre """

    graph={0:[]}
    pere={0:[]}
    t=1
    while(t!=n):

        r=randrange(0,t,1)
        print("rand \(r) ")
        print(r)
        if(len(pere[r])==0):#pas de pere on applique Tc
            graph[t]=[r]
            pere[r]+=[t]
            pere[t]=[]
        elif(len(graph[r])==1):#si le noeud n'a qu'un seul fils j'applique Ic
             graph[t]=graph[r]
             pere[graph[r][0]]+=[t]
             
             graph[r]=[t]
             pere[t]=[r]
             
             pere[graph[r][0]].remove(r)
             pere[graph[r][0]]+=[t]
        else:# On applique Bc
             graph[r]= graph[r]+[t]
             pere[t]=[r]
             graph[t]=[]
        t+=1
    return (graph,pere)

generator(12)
#
