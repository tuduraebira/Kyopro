N = int(input())
a = list(map(int, input().split()))

rui = [0]
wa = 0
for n in a:
    wa += n
    rui.append(wa)

mi = 10 ** 32
for i in range(1, N):
    mi = min(mi, abs((rui[i] - rui[0]) - (rui[N] - rui[i])))

print(mi)