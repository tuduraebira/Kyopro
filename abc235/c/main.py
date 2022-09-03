from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
D = defaultdict(list)
for i, x in enumerate(A, 1):
    D[x].append(i)

for _ in range(Q):
    x, k = map(int, input().split())
    if k <= len(D[x]):
        print(D[x][k - 1])
    else:
        print(-1)