N, M = map(int, input().split())
a = set()
for _ in range(M):
    aa = int(input())
    a.add(aa)
mod = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    if i not in a:
        dp[i] += dp[i - 1]
        dp[i] %= mod
        if i >= 2:
            dp[i] += dp[i - 2]
            dp[i] %= mod

print(dp[N])