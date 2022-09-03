from math import ceil, floor


N, M = map(int, input().split())
A = list(map(int, input().split()))

rui = [0]
r = 0
for a in A:
    r += a
    rui.append(r)

ans = 0
for i in range(M):
    ans += (i + 1) * A[i]

ne = ans
for i in range(N - M):
    a = ne
    a -= (rui[i + M] - rui[i])
    a += (M * A[i + M])
    #print(a)
    ans = max(a, ans)
    ne = a

print(ans)