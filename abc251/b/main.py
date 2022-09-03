from itertools import combinations


N, W = map(int, input().split())
A = list(map(int, input().split()))

s = set()

for a in A:
    if a <= W:
        s.add(a)

for b in combinations(A, 2):
    if sum(b) <= W:
        s.add(sum(b))

for c in combinations(A, 3):
    if sum(c) <= W:
        s.add(sum(c))

print(len(s))