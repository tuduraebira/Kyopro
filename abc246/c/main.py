N, K, X = map(int, input().split())
A = list(map(int, input().split()))

#As = sorted(A, reverse=True)
#print(As)

for i in range(N):
    while 0 < K and 0 <= A[i] - X:
        A[i] -= X
        K -= 1

As = sorted(A)

if N > K:
    print(sum(As[:N - K]))
else:
    print(0)