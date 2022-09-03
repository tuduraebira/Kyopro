from collections import defaultdict


N = int(input())
a = list(map(int, input().split()))

cnt = defaultdict(int)
for an in a:
    cnt[an] += 1

ans = 0
for k, v in cnt.items():
    if k == v:
        continue
    elif k < v:
        ans += (v - k)
    else:
        ans += v

print(ans)