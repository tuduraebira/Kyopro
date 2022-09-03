N = int(input())
xyP = [list(map(int, input().split())) for _ in range(N)]

power = [10 ** 20] * N
for i in range(N):
    x1, y1, P1 = xyP[i]

    for j in range(N):
        if i == j:
            continue
        x2, y2, P2 = xyP[j]

        dist = abs(x1 - x2) + abs(y1 - y2)
        if dist % P1 == 0:
            power[j] = min(power[j], dist // P1)
        else:
            power[j] = min(power[j], dist // P1 + 1)

ans = 10 ** 20
for i in range(len(power)):
    s = set(power)
    s.remove(power[i])
    ans = min(ans, max(s))

print(ans)