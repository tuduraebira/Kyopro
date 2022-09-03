N, C = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

ran = {}
for a, b, c in info:
    if ran.get(a) == None:
        ran[a] = c
    else:
        ran[a] += c

    if ran.get(b + 1) == None:
        ran[b + 1] = -c
    else:
        ran[b + 1] += -c

ran = sorted(ran.items())

pri = 0
pd = 0
ans = 0
for d, p in ran:
    if pri >= C:
        ans += C * (d - pd)
    else:
        ans += pri * (d - pd)

    pri += p
    pd = d

print(ans)