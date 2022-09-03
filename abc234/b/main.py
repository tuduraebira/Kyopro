from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

N = int(input())
P = []
for _ in range(N):
    x, y = map(float, input().split())
    P.append([x, y])

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans = max(ans, dist(P[i][0], P[i][1], P[j][0], P[j][1]))

print(ans)