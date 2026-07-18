def Floyd_warsall(w,n):
    D=[]
    for i in range(n+1):
        row=[]
        for j in range(n+1):
            row.append(w[i][j])
        D.append(row)
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if D[i][k]+ D[k][j] < D[i][j]:
                    D[i][j]=D[i][k]+D[k][j]
    return D

INF=float('inf')
n=4
W=[
    [INF,INF,INF,INF,INF],
    [INF,0,INF,3,INF],
    [INF,2,0,INF,INF],
    [INF,INF,7,0,1],
    [INF,6,INF,INF,0]
]

d=Floyd_warsall(W,n)
for i in range(1,n+1):
    for j in range(1,n+1):
        print(d[i][j],end='\t')
    print()