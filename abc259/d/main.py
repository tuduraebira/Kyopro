from math import sqrt
import sys
sys.setrecursionlimit(10**7)

N = int(input())
sx, sy, tx, ty = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        dist = abs(p[i][0] - p[j][0]) ** 2 + abs(p[i][1] - p[j][1]) ** 2
        if (p[i][2] - p[j][2]) ** 2 <= dist and dist <= (p[i][2] + p[j][2]) ** 2:
            G[i].append(j)
            G[j].append(i)

s = []
g = []
for i, pt in enumerate(p):
    x = pt[0]
    y = pt[1]
    r = pt[2]
    if (sx - x) ** 2 + (sy - y) ** 2 == r ** 2:
        s.append(i)
    if (tx - x) ** 2 + (ty - y) ** 2 == r ** 2:
        g.append(i)

for ss in s:
    if ss in g:
        print('Yes')
        exit()
#print(G, s, g)

isC = [False] * N
def dfs(pt):
    if pt in g:
        print('Yes')
        exit()

    isC[pt] = True

    for ppt in G[pt]:
        #print(ppt)
        if isC[ppt] == True:
            continue
        dfs(ppt)

for pt in s:
    dfs(pt)

print('No')