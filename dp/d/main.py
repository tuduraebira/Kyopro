N, W = map(int, input().split())
wv = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, W + 1):
        if j - wv[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wv[i][0]] + wv[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[N]))