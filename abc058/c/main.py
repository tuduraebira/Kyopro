from collections import defaultdict


n = int(input())
ch_cnt = defaultdict(list)
for _ in range(n):
    S = input()
    cnt_tmp = defaultdict(int)
    for s in S:
        cnt_tmp[s] += 1

    for k, v in cnt_tmp.items():
        ch_cnt[k].append(v)

#print(ch_cnt)
ans = ''
for k, v in ch_cnt.items():
    num = 0
    if len(v) == n:
        num = min(v)
    ans += k * num

print(''.join(sorted(ans)))