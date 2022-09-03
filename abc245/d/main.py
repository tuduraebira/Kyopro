from numpy import poly1d


N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

polyA = poly1d(list(reversed(A)))
polyC = poly1d(list(reversed(C)))

polyB = polyC / polyA
coefB = list(map(int, polyB[0].c))

ans = list(reversed(coefB))
print(*ans)