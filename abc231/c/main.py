from bisect import bisect, bisect_left


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    x = int(input())
    cnt = bisect_left(A, x)
    print(N - cnt)