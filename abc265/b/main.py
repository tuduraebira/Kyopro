N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split()))
XY = [0] * N
for _ in range(M):
    X, Y = map(int, input().split())
    XY[X - 1] = Y

for i in range(N):
    T -= A[i]

    if T <= 0:
        print('No')
        exit()

    T += XY[i]

print('Yes')