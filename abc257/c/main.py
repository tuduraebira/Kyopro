from bisect import bisect_left


N = int(input())
S = input()
W = list(map(int, input().split()))

oc = []
for w, s in zip(W, S):
    oc.append([w, s])

oc.sort()
W.sort()
Sx = []

kugiri = 0
rui = [kugiri]
for l in oc:
    kugiri += int(l[1])
    rui.append(kugiri)

ans = rui[-1]
for i in range(N):
    k = W[i] + 0.5
    j = bisect_left(W, k)
    ans = max(ans, j - (rui[j] - rui[0]) + (rui[-1] - rui[j]))


print(ans)