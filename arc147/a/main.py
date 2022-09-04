N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ma = max(A)
mi = min(A)
ma_pt = 0
mi_pt = len(A) - 1
ans = 0
while True:
    if ma_pt == mi_pt:
        break

    ans += 1
    if A[ma_pt] % A[mi_pt] == 0:
        ma_pt += 1
        ma = A[ma_pt]
    else:
        A.append(A[ma_pt] % A[mi_pt])
        mi_pt += 1
        ma_pt += 1
        ma = A[ma_pt]

print(ans)