N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (2 * 10 ** 5 + 10)
for a in A:
    cnt[a] += 1

ans = N * (N - 1) * (N - 2) // 6
for i in cnt:
    ans -= i * (i - 1) // 2 * (N - i)
    ans -= i * (i - 1) * (i - 2) // 6

print(ans)