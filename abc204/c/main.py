import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)

def dfs(v):
    if temp[v]: return
    temp[v] = True
    for vv in G[v]: dfs(vv)

ans = 0
for i in range(N):
    temp = [False] * N
    dfs(i)
    ans += sum(temp)

print(ans)