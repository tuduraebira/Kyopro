N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
info = [[0] * 5 for _ in range(10 ** 5 + 20)]
maT = -1
for T, X, A in L:
    maT = max(maT, T)
    if T < X:
        continue
    info[T][X] = A

dp = [[0] * 5 for _ in range(10 ** 5 + 10)]
for t in range(1, 10 ** 5 + 1):
    for index in range(5):
        if index == 0:
            dp[t][index] = max(dp[t - 1][index] + info[t][index], dp[t - 1][index + 1] + info[t][index])
        elif index == 4:
            dp[t][index] = max(dp[t - 1][index] + info[t][index], dp[t - 1][index - 1] + info[t][index])
        else:
            dp[t][index] = max(max(dp[t - 1][index] + info[t][index], dp[t - 1][index + 1] + info[t][index]), dp[t - 1][index - 1] + info[t][index])

# print(info[:10])
# print(dp[:10])
print(max(dp[maT]))