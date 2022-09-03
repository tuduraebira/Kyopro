N, M = map(int, input().split())
teiki = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N + 1)]
for a, b in teiki:
    G[a].append(b)
    G[b].append(a)
flag = [False] * (N + 1)

def dfs(x, d):
    d += 1

    if flag[x] == True:
        return

    if x == N:
        print("POSSIBLE")
        exit()

    if d > 2:
        d -= 1
        return
    
    flag[x] = True
    for g in G[x]:
        dfs(g, d)

dfs(1, 0)
print("IMPOSSIBLE")
