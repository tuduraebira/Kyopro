import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())
def f(n):
    return int(n) - 1
xy = [list(map(f, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for x, y in xy:
    G[x].append(y)

visit = [-1 for _ in range(N)]

def dfs(x):
    if visit[x] != -1:
        return visit[x]
    c = 0
    for j in G[x]:
        c = max(c, dfs(j))
    visit[x] = c + 1
    return c + 1

for i in range(N):
    if visit[i] == -1:
        dfs(i)

ans = 0
for i in range(N):
    ans = max(ans, visit[i])

print(ans - 1)