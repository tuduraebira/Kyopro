INF = 1 << 60

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
dp = [[-INF] * W for _ in range(H)]
dp[0][0] = 1

for row in range(H):
    for col in range(W):
        if row == col == 0:
            continue
        if C[row][col] == ".":
            d1 = dp[row - 1][col] if row - 1 >= 0 else -INF
            d2 = dp[row][col - 1] if col - 1 >= 0 else - INF
            dp[row][col] = max(d1, d2) + 1

ans = 0
for dp_row in dp:
    ans = max(ans, *dp_row)
print(ans)