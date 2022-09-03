N = int(input())
S = input()
muki = []
wa = []
for s in S:
    if s == 'W':
        muki.append(1)
    else:
        muki.append(0)
wa_tmp = 0
wa.append(wa_tmp)
for m in muki:
    wa_tmp += m
    wa.append(wa_tmp)

ans = 10 ** 18
for i in range(N):
    tmp = (wa[i] - wa[0]) + ((N - i - 1) - (wa[N] - wa[i + 1]))
    ans = min(ans, tmp)

print(ans)