N, K = map(int, input().split())
A = list(map(int, input().split()))

p = []
for i, a in enumerate(A):
    p.append([a, -i])
p.sort()

i_max = -1
flag = False
ans = 10 ** 31
for a, i in p:
    i = -i
    if K <= i:
        if i_max != -1:
            flag = True
            ans = min(ans, i - i_max)

    if i < K:
        i_max = max(i_max, i)

if not flag:
    print(-1)
else:
    print(ans)