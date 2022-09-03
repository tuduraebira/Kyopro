xy = [list(map(int, input().split())) for _ in range(3)]

xp = {}
yp = {}
for x, y in xy:
    if xp.get(x) == None:
        xp[x] = 1
    else:
        xp[x] += 1

    if yp.get(y) == None:
        yp[y] = 1
    else:
        yp[y] += 1

for i, j in xp.items():
    if j == 1:
        x = i

for i, j in yp.items():
    if j == 1:
        y = i

print(x, y)