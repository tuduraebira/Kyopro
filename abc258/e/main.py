N, Q, X = map(int, input().split())
W = list(map(int, input().split()))
kol = []
p = 0
ko = 0
weight = 0
while True:
    ko += 1
    weight += W[p]
    if weight >= X:
        kol.append(ko)
        if p == N - 1:
            break
        p = 0
        weight = 0
    p += 1

for _ in range(Q):
    K = int(input())

    print(kol[(K - 1) % len(kol)])