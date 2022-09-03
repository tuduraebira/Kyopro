N = int(input())
A = list(map(int, input().split()))

cnt = {}
v = []
for a in A:
    if cnt.get(a) == None:
        cnt[a] = 1
    else:
        cnt[a] += 1

    if cnt[a] == 2:
        v.append(a)
        cnt[a] = 0
vs = sorted(v, reverse=True)

ans = 0
if len(v) >= 2:
    ans = vs[0] * vs[1]
print(ans)