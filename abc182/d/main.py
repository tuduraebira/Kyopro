N = int(input())
A = list(map(int, input().split()))

p = []
q = []
ma = 0
wa = 0
for a in A:
    wa += a
    p.append(wa)
    ma = max(ma, wa)
    q.append(ma)

r = 0
x = 0
for i in range(N):
    r = max(r, x + q[i])
    x = x + p[i]

print(r)