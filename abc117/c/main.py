N, M = map(int, input().split())
X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit()

X.sort()
sa = []
for i in range(M - 1):
    sa.append(abs(X[i] - X[i + 1]))
sa.sort(reverse=True)

print(sum(sa[N - 1:]))