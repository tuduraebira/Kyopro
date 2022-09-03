X, Y, N = map(int, input().split())

if N <= 2:
    print(N * X)
elif 3 * X <= Y:
    print(N * X)
else:
    shou = N // 3
    amari = N % 3
    print(shou * Y + amari * X)