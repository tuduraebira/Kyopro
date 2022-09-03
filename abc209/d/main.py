from collections import deque


N, Q = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

query = [list(map(int, input().split())) for _ in range(Q)]

color = [-1] * (N + 1)
color[0] = 0
color[1] = 0

deq = deque()
deq.append(1)

while deq:
    v = deq.popleft()
    for i in G[v]:
        if color[i] != -1:
            continue
        color[i] = 1 - color[v]
        deq.append(i)

for c, d in query:
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")