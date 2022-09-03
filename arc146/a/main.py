import itertools


N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ma = -1
for a, b, c in itertools.permutations([A[0], A[1], A[2]], 3):
    #print(a, b, c)
    ma = max(ma, int(str(a) + str(b) + str(c)))

print(ma)