S = input()
T = input()

s_cnt = []
t_cnt = []
prev = ''

for s in S:
    if prev == s:
        s_cnt[-1][1] += 1
    else:
        s_cnt.append([s, 1])
        prev = s

prev = ''
for t in T:
    if prev == t:
        t_cnt[-1][1] += 1
    else:
        t_cnt.append([t, 1])
        prev = t

if len(s_cnt) != len(t_cnt):
    print('No')
    exit()

for sl, tl in zip(s_cnt, t_cnt):
    if sl[0] == tl[0]:
        if sl[1] == tl[1]:
            continue
        elif sl[1] == 1 and tl[1] > 1:
            print('No')
            exit()
        elif sl[1] > tl[1]:
            print('No')
            exit()
        else:
            continue
    else:
        print('No')
        exit()

print('Yes')