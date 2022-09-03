N, M, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
keta = len(bin(A[0] + M)[2:])

keta_list = []
keta_n = -1


for ke in range(keta, 0, -1):
    res = 0
    res_l = []
    for k in range(K):
        r = (2 ** (ke - 1)) - A[k]
        if r < 0:
            res_l.append(0)
        else:
            res += r
            res_l.append(r)
    
    if res > M:
        continue
    else:
        keta_n = ke
        keta_list.append(ke)

    for i, re in enumerate(res_l):
        b = bin(A[i])[2:]
        if len(b) >= ke and b[len(b) - ke] == '1':
            continue
        else:
            A[i] += re
            A[i] -= 2 ** (ke - 1)
            M -= re

print(keta_list)