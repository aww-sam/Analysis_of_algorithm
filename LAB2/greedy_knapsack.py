def greedy_knapsack(X:list,V:list,W:list,M):
    n=len(X)
    items=[]
    for i in range(n):
        ratio= V[i]/W[i]
        items.append((ratio,X[i],V[i],W[i]))
    items.sort(reverse=True)
    S=[]
    SW=0
    SP=0
    i=0
    while i<n:
        ratio,x,p,w=items[i]
        if (SW+w)<=M:

            S.append(x)
            SW=SW+w
            SP=SP+p

        else:

            frac=(M-SW)/w
            S.append((x,frac))
            SW=SW+w*frac
            SP=SP+p*frac

            break
        i=i+1

    return S,SW,SP

X=['x1','x2','x3','x4','x5','x6','x7']
V=[9,5,2,7,6,16,3]
W=[2,5,6,11,1,9,1]
M=28

s,sw,sp=greedy_knapsack(X,V,W,M)
print('S:',s)
print('SW:',sw)
print('SP:',sp)