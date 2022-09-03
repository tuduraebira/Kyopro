N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-(10 ** 32)] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(M + 1):
        if j <= i:
            if j == M:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (j + 1) * A[i])

print(dp[N][M])