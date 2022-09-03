N, M = map(int, input().split())

if N * 2 >= M:
    print(M // 2)
    exit()
else:
    scc = N
    M -= (N * 2)
    scc += (M // 4)
    print(scc)
    exit()