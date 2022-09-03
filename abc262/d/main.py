N = int(input())
a = list(map(int, input().split()))

mod = 998244353
ans = 0

for i in range(2 ** N):
    sm = 0
    cnt = 0
    for j in range(N):
        if ((i >> j) & 1):
            sm += a[j]
            cnt += 1
    print(sm, cnt)
    if cnt != 0 and sm % cnt == 0:
        ans += 1
        ans %= mod

print(ans)