from bisect import bisect_left, bisect_right


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
rui = [0]
su = 0
for a in A:
    su += a
    rui.append(su)

for _ in range(Q):
    X = int(input())

    l = bisect_left(A, X)
    r = bisect_right(A, X)

    #print(l, r)
    print(X * l - (rui[l] - rui[0]) + (rui[-1] - rui[r]) - X * (N - r))