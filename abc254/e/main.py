from queue import Queue


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
dis = [-1] * (N + 1)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())

    q = Queue()
    q.put(x)
    dis[x] = 0
    vs = []
    while not q.empty():
        u = q.get()

        vs.append(u)
        if dis[u] == k:
            continue

        for j in range(len(G[u])):
            v = G[u][j]
            if dis[v] != -1:
                continue
            dis[v] = dis[u] + 1
            q.put(v)

    ans = 0
    for j in range(len(vs)):
        ans += vs[j]
        dis[vs[j]] = -1

    print(ans)