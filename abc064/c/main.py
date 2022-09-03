from collections import defaultdict


N = int(input())
a = list(map(int, input().split()))

rng_num = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
kind = defaultdict(int)
for n in a:
    for i, rng in enumerate(rng_num):
        if 3200 <= n:
            kind[8] += 1
            break
        if rng - 400 <= n < rng:
            kind[i] += 1
#print(kind)

if kind.get(8) != None:
    not_free_cnt = len(kind) - 1
    free_cnt = kind[8]
else:
    print(len(kind), len(kind))
    exit()

mi = 10 * 18
ma = -1

if not_free_cnt == 0:
    mi = 1
else:
    mi = not_free_cnt
ma = not_free_cnt + free_cnt

print(mi, ma)