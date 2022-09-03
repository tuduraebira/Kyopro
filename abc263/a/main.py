cards = list(map(int, input().split()))

d = {}
for c in cards:
    if d.get(c) == None:
        d[c] = 1
    else:
        d[c] += 1

if len(d) == 2:
    is2 = False
    is3 = False
    for v in d.values():
        if v == 2:
            is2 = True
        if v == 3:
            is3 = True

    if is2 and is3:
        print('Yes')
    else:
        print('No')
else:
    print('No')