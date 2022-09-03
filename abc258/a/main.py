K = int(input())

H = 21
M = 0

if K >= 60:
    H += 1
    M += (K % 60)
    if len(str(M)) < 2:
        print(f'{H}:0{M}')
    else:
        print(f'{H}:{M}')
else:
    M += K
    if len(str(M)) < 2:
        print(f'{H}:0{M}')
    else:
        print(f'{H}:{M}')