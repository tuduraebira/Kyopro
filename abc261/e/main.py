N, C = map(int, input().split())
TA = [list(map(int, input().split())) for _ in range(N)]

num = 0
l = []
for t, a in TA:
    if t == 1:
        num = num & a
    elif t == 2:
        num = num | a
    elif t == 3:
        num = num ^ a
    l.append(num)

for n, ll in zip(l, TA):
    if ll[0] == 1:
        C = C & n
    elif ll[0] == 2:
        C = C | n
    elif ll[0] == 3:
        C = C ^ n
    print(C)