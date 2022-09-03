N, L, R = map(int, input().split())
A = list(map(int, input().split()))

def LO(Li):
    rui = [0]
    tmp = 0
    for a in Li:
        tmp += a
        rui.append(tmp)

    ma_x = -(10 ** 50)
    index_x = -1
    for i in range(1, N + 1):
        if ma_x < (rui[i] - rui[0]) - L * i:
            ma_x = (rui[i] - rui[0]) - L * i
            index_x = i
    xA = []
    if ma_x >= 0:
        xA = [L] * index_x + Li[index_x:]
    else:
        xA = Li

    return xA

def RO(Li):
    rui2 = [0]
    tmp2 = 0
    for xa in Li:
        tmp2 += xa
        rui2.append(tmp2)

    ma_y = -(10 ** 50)
    index_y = -1
    for i in range(N - 1, -1, -1):
        if ma_y < (rui2[-1] - rui2[i]) - R * (N - i):
            ma_y = (rui2[-1] - rui2[i]) - R * (N - i)
            index_y = i

    xyA = []
    if ma_y >= 0:
        xyA = Li[:index_y] + [R] * (N - index_y)
    else:
        xyA = Li

    return xyA

t1 = LO(A)
t2 = RO(t1)

s1 = RO(A)
s2 = LO(s1)

print(min(sum(t2), sum(s2)))