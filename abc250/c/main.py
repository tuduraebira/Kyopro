N, Q = map(int, input().split())
query = []
for _ in range(Q):
    query.append(int(input()))

num = [i for i in range(1, N + 1)]
pos = [i for i in range(1, N + 1)]

for q in query:
    p = pos[q - 1]
    if p == N:
        p -= 1

    l = num[p - 1]
    r = num[p]
    num[p - 1], num[p] = num[p], num[p - 1]


    pos[l - 1] += 1
    pos[r - 1] -= 1

    #print(p, q)

print(*num)