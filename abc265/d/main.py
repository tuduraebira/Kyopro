from bisect import bisect_left


N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

rui = []
rui_tmp = 0
rui.append(rui_tmp)
for a in A:
    rui_tmp += a
    rui.append(rui_tmp)

for i in range(len(A)):
    l = i
    r = bisect_left(rui, P + A[l])
    print(r)
    if r >= len(rui):
        continue

    if rui[r] - rui[l] == P:
        #print('P', l, r)
        l = r
    else:
        continue

    r = bisect_left(rui, Q + A[l])
    if r >= len(rui):
        continue
    if rui[r] - rui[l] == Q:
        #print('Q', l, r)
        l = r
    else:
        continue

    r = bisect_left(rui, R + A[l])
    if r >= len(rui):
        continue
    if rui[r] - rui[l] == R:
        #print('R', l, r)
        print('Yes')
        exit()
    else:
        continue

print('No')