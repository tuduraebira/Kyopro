# from math import sqrt

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# XY = [list(map(int, input().split())) for _ in range(N)]
# light = [False] * N
# for a in A:
#     light[a - 1] = True

# ans = 0
# for i in range(N):
#     tmp = 1000000
#     isc = False
#     for j in range(N):
#         if i == j or light[i]:
#             continue

#         dist = sqrt((abs(XY[i][0] - XY[j][0])) * (abs(XY[i][0] - XY[j][0])) + (abs(XY[i][1] - XY[j][1])) * (abs(XY[i][1] - XY[j][1])))
#         #print(i, j, dist)
#         if light[j]:
#             tmp = min(tmp, dist)
#             isc = True

#     if isc:
#         ans = max(ans, tmp)

# print(ans)
import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
pos = [list(map(int,input().split())) for _ in range(N)]

dislist = set()
for j in range(N):
    dis = []
    for i in A:
        dist = abs(pos[i-1][0]-pos[j][0])**2 + abs(pos[i-1][1]-pos[j][1])**2
        dis.append(math.sqrt(dist))

    dislist.add(min(dis))
    
print(max(dislist))