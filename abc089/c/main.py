from collections import defaultdict


N = int(input())
S = [input() for _ in range(N)]

march = "MARCH"
cnt = defaultdict(int)
for s in S:
    cnt[s[0]] += 1
#print(cnt)

ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += cnt[march[i]] * cnt[march[j]] * cnt[march[k]]

print(ans)