def Floyd_warsall(w, n):
    D = [row[:] for row in w]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    return D


INF = float('inf')
n = 4
W = [
    [0, INF, 3, INF],
    [2, 0, INF, INF],
    [INF, 7, 0, 1],
    [6, INF, INF, 0]
]

d = Floyd_warsall(W, n)
for i in range(n):
    for j in range(n):
        print(d[i][j], end='\t')
    print()