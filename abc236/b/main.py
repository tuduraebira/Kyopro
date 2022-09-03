N = int(input())
A = list(map(int, input().split()))

cnt = [0 for _ in range(N)]
for i in A:
    cnt[i - 1] += 1

for i, c in enumerate(cnt):
    if c < 4:
        ans = i + 1

print(ans)