N, M, X = map(int, input().split())
C, A = [], []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

is_match = False
ans = 10 ** 18
for i in range(1 << N):
    us = [0] * M
    price = 0

    for j in range(N):
        if ((i >> j) & 1):
            for k in range(M):
                us[k] += A[j][k]
            price += C[j]

    if all(a >= X for a in us):
        ans = min(ans, price)
        is_match = True

if is_match:
    print(ans)
else:
    print(-1)