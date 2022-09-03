mod = 10 ** 9 + 7

N, M = map(int, input().split())
if abs(N - M) > 1:
    print(0)
    exit()

ans = 1
if N == M:
    for i in range(1, N + 1):
        ans *= (i * i)
        ans %= mod
    ans *= 2
    ans %= mod
    print(ans)
else:
    ma = max(N, M)
    for i in range(1, ma):
        ans *= (i * i)
        ans %= mod
    ans *= ma
    ans %= mod
    print(ans)