N = int(input())
cnt = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

for c in cnt:
    if c == N - 1:
        print("Yes")
        exit()
print("No")