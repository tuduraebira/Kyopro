N = int(input())
aoki = 0
hyou = []
eikyou = []
for _ in range(N):
    A, B = map(int, input().split())
    aoki += A
    eikyou.append(2 * A + B)
    hyou.append([A, B])

eikyou.sort(reverse=True)
ans = 0
while aoki >= 0:
    aoki -= eikyou[ans]
    ans += 1

print(ans)