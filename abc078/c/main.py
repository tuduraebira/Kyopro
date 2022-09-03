N, M = map(int, input().split())

cnt = 2 ** M
t = 1900 * M + 100 * (N - M)
print(cnt * t)