from collections import defaultdict


N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(1 << N):
    a = 0
    cnt = defaultdict(int)
    for j in range(N):
        if (i >> j) & 1:
            for s in S[j]:
                cnt[s] += 1

    for c in cnt.values():
        if c == K:
            a += 1

    ans = max(ans, a)

print(ans)