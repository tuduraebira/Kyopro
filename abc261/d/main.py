N, M = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(M)]
d = {}
for c, y in CY:
    d[c] = y

# dp = [[[0] * 2 for _ in range(N + 1)] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(N + 1):
#         dp[i][j][0] = max(dp[i - 1][0], dp[i - 1][1]) + X[i - 1]
#         dp[i][j][1] = max(dp[i - 1][0], dp[i - 1][1])
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(i + 1):
        if j + 1 in d:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i] + d[j + 1])
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])

#print(dp)
print(max(dp[N]))