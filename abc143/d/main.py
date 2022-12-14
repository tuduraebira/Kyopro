from bisect import bisect_left
from itertools import combinations


N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        k = bisect_left(L, L[i] + L[j])
        ans += max(k - (j + 1), 0)

print(ans)