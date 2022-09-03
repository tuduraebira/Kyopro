N, K = map(int, input().split())

if K < 0:
    K = -K

num = [0] * (N * 2 + 1)
for n in range(2, N * 2 + 1):
    num[n] = min(n - 1, N * 2 + 1 - n)
ans = 0
for n in range(K, N * 2 + 1):
    ans += num[n] * num[n - K]
print(ans)