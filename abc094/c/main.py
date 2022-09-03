N = int(input())
X = list(map(int, input().split()))
Xs = sorted(X)

l = Xs[N // 2 - 1]
h = Xs[N // 2]

for i in range(N):
    if X[i] <= l:
        print(h)
    else:
        print(l)