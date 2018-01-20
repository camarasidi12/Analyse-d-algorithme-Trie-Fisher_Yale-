#coding:utf8

def bfs(G,s) :
    """ parcourt du grapht"""
    P,Q={s:None},[s]
    while Q:
        u=Q.pop(0)
        for v in G[u]:
            if v in P : continue
            P[v]=u
            Q.append(v)
    return P

def existChemin(P,s,fils,E):

    """Verifie s'il existe un chemin entre deux sommets du graphe"""
    
    for p in P[s]:
        if(p in E[fils]):
            return True
        else:
            return False

def isFreeCycle(G,P):
    """Verifie si le graphe est free-cycle ou non"""
    print(G.keys())
    if(len(G.keys())<=1):
        return True
    
    for s in G.keys():
        
        
        """print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(s)
        print(G[s])
        print(P[s])
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")"""
        

        #if(len(G[s])==0 and (len(P[s])==1 or len(P[s]==0))): #Bottom
        if(len(G[s])==0 and len(P[s])==1): #Bottom
            #G.pop(s)
            #P.pop(s)
            remove(P,G,s)
            return isFreeCycle(G,P)
        elif(len(G[s])<=1 and len(P[s])==0): #Top
            remove(P,G,s)
            #G.pop(s)
            #P.pop(s)
            return isFreeCycle(G,P)
        elif(len(G[s])==1 and len(P[s])==1):
            fils=G[s][0]
            if( not (P[s][0] in P[fils])):
                # if(not existChemin(P,s,fils,E)):
                G[P[s][0]]=G[P[s][0]]+G[s]
            #G.pop(s)
            #P.pop(s)
            remove(P,G,s)
            return isFreeCycle(G,P)

        else: continue
    return False

def remove(P,G,e):
    """ enlve l'element supprimer en tanqu parent"""
    for i in G[e]:
        P[i].remove(e)
    for i in P[e]:
        G[i].remove(e)
    G.pop(e)
    P.pop(e)


G={'a':['aa','b'],'aa':['aaa'],'aaa':['aaaa'],'b':[],'aaaa':[]}
P={'a':[],'aa':['a'],'aaa':['aa'],'aaaa':['aaa'], 'b':['a']}
#E={'a':[],'aa':['a'],'aaa':['aa','a'],'aaaa':['aa','a','aaa'], 'b':['a']}

GG={1:[2,3],2:[],3:[4],4:[]}
PP={2:[1],3:[1],1:[], 4:[3]}

G={'a':['b','c','r'],'b':['d'],'c':['d','e'],'d':['f'] ,'e':[],'f':[],'r':[] }
P={'a':[],'b':['a'],'c':['a'],'d':['b','c'],'e':['c'],'f':['d'],'r':['a']}

A={1:[2,3],4:[3],2:[],3:[]}
B={2:[1],3:[1,4],1:[],4:[]}
g=dict()
g['a']=["a"]
g['a']=["b"]+g['a']
print(isFreeCycle(A,B))








