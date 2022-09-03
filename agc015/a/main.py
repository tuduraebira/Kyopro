N, A, B = map(int, input().split())

if A > B or (N == 1 and A != B):
    print(0)
    exit()

mi = A * (N - 1) + B
ma = A + B * (N - 1)

print(ma - mi + 1)