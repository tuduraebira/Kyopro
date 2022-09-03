L, R = map(int, input().split())

if R - L > 3000:
    print(0)
    exit()

res = 2018
for i in range(L, R):
    for j in range(i + 1, R + 1):
        res = min(res, (i * j) % 2019)
print(res)