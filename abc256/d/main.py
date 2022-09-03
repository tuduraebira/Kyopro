N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort()

l = XY[0][0]
r = XY[0][1]
for i in range(N - 1):
    if r >= XY[i + 1][0]:
        r = max(r, XY[i + 1][1])
    else:
        print(l, r)
        l = XY[i + 1][0]
        r = XY[i + 1][1]

print(l, r)