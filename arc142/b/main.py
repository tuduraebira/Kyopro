N = int(input())
x = [-1] * N
ans = []

pos = 0
v = 1
while True:
    x[pos] = v
    pos += 2
    v += 1 
    if pos >= N:
        break
pos = 1
while True:
    x[pos] = v
    pos += 2
    v += 1
    if pos >= N:
        break

ans.append(x)
for i in range(N - 1):
    l = list(map(lambda y: y + (i + 1) * N, x))
    ans.append(l)

for l in ans:
    print(*l)