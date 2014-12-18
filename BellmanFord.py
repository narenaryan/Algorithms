def Bellman_Ford(G,S):
    weight,pred={},{}
    for v in G.keys():
        if v==S: weight[v]=0
        else: weight[v]=10
        pred[v]=None

    for i in range(1,len(G.keys())-1):
        for k,v in G.items():
            for k1,v1 in v.items():
                if weight[k]+v1<weight[k1]:
                    weight[k1]=weight[k]+v1
                    pred[k1]=k
    return weight,pred

def shortestPath(G,start,end):
    D,P = Bellman_Ford(G,start)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        end = P[end]
    Path.reverse()
    return Path


#Graph structure is a dictionary.

F1={'S':{'A':4,'B':6},
    'A':{'C':2,'D':1},
    'B':{'A':2,'D':2},
    'C':{'T':3,'D':1},
    'D':{'T':7},
    'T':{}
}

print shortestPath(F1,'S','T')#Finds shortest path from S to T in graph F1
