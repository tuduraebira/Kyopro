from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

pos = [[] for _ in range(2 * (10 ** 5) + 1)]
for i, a in enumerate(A):
    pos[a].append(i)
#print(pos)

for L, R, X in query:
    l = bisect_left(pos[X], L - 1)
    r = bisect_left(pos[X], R)
    print(r - l)