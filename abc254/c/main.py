N, K = map(int, input().split())
a = list(map(int, input().split()))

num = [[] for _ in range(K)]
for i, n in enumerate(a):
    num[i % K].append(n)

for i in range(K):
    num[i].sort()

for i in range(N - 1):
    i_next = i + 1
    if num[i % K][i // K] > num[i_next % K][i_next // K]:
        print("No")
        exit()

print("Yes")