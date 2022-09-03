INF = 1 << 62 - 1 << 31
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [INF] * (N + 1)

dp[1] = 0
for i in range(2, N + 1):
    if i > K:
        for j in range(K):
            dp[i] = min(dp[i], dp[i - (j + 1)] + abs(h[i - (j + 1) - 1] - h[i - 1]))
    else:
        for j in range(i - 1):
            dp[i] = min(dp[i], dp[i - (j + 1)] + abs(h[i - (j + 1) - 1] - h[i - 1]))

print(dp[-1])