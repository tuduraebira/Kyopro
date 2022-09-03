N = int(input())
h = list(map(int, input().split()))
dp = [0] * (N + 1)

dp[0] = 0
dp[1] = 0
for i in range(2, N + 1):
    if i >= 3:
        dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i - 2]), dp[i - 2] + abs(h[i - 1] - h[i - 3]))
    else:
        dp[i] = dp[i - 1] + abs(h[i - 1] - h[i - 2])

print(dp[N])