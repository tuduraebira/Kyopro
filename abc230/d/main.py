from operator import itemgetter

N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=itemgetter(1))

ans = 0
x = 0

for l, r in LR:
    if x < l:
        ans += 1
        x = r + D - 1

print(ans)