N = int(input())
abc = [[0, 0, 0, 0]] + [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (3 + 1) for _ in range(N + 1)]
for x in range(3 + 1):
    dp[0][x] = 0

"""
1 = A
2 = B
3 = C
"""
for i in range(1, N + 1):
    for j in range(1, 3 + 1):
        if j == 1:
            dp[i][j] = max(dp[i - 1][2] + abc[i][j], dp[i - 1][3] + abc[i][j])
        elif j == 2:
            dp[i][j] = max(dp[i - 1][1] + abc[i][j], dp[i - 1][3] + abc[i][j])
        else:
            dp[i][j] = max(dp[i - 1][1] + abc[i][j], dp[i - 1][2] + abc[i][j])

print(max(dp[N]))