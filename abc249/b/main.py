from collections import defaultdict


S = input()

cnt = defaultdict(int)
for s in S:
    cnt[s] += 1

if not S.islower() and not S.isupper() and len(cnt) == len(S):
    print("Yes")
else:
    print("No")