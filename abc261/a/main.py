L1, R1, L2, R2 = map(int, input().split())

if L1 > L2:
    tmp = L1
    L1 = L2
    L2 = tmp
    tmp = R1
    R1 = R2
    R2 = tmp

if R1 <= R2:
    if R1 - L2 > 0:
        print(R1 - L2)
    else:
        print(0)
else:
    if R2 - L2 > 0:
        print(R2 - L2)
    else:
        print(0)