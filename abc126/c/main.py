N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    y = i
    q = 1 / N
    while y < K:
        y *= 2
        q /= 2
    ans += q

print(ans)