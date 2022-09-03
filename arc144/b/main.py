from math import ceil, floor


N, a, b = map(int, input().split())
A = list(map(int, input().split()))

l = min(A)
r = max(sum(A) // N + 1, max(A))
while r - l > 1:
    mid = (l + r) // 2
    x = 0
    y = 0
    for ai in A:
        if ai < mid:
            x += ceil((mid - ai) / a)
        else:
            y += floor((ai - mid) / b)

    if x <= y:
        l = mid
    else:
        r = mid

print(l)
