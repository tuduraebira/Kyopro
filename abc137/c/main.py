from collections import defaultdict


N = int(input())
ch = defaultdict(int)
for _ in range(N):
    s = input()
    ss = sorted(s)
    ch[str(ss)] += 1

ans = 0
for v in ch.values():
    ans += (v * (v - 1) // 2)
print(ans)