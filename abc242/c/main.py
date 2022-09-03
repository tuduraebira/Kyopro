mod = 998244353

N = int(input())

dp = [[0] * 11 for _ in range(N + 1)]

for k in range(1, 10):
    dp[1][k] = 1

for n in range(2, N + 1):
    for k in range(1, 10):
        dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k] + dp[n - 1][k + 1]
        dp[n][k] %= mod

ans = 0
for k in range(1, 10):
    ans += dp[N][k]
    ans %= mod

print(ans)