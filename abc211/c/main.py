mod = 10 ** 9 + 7

S = input()
N = len(S)
T = 'chokudai'
M = len(T)
dp = [[0] * (M + 1) for _ in range(N + 1)]
#print(dp)

S = '*' + S
T = '*' + T

for x in range(N + 1):
    dp[x][0] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if S[i] != T[j]:
            dp[i][j] = dp[i - 1][j]
        if S[i] == T[j]:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod

print(dp[N][8])