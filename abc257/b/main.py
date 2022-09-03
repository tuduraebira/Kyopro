N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for l in L:
    index = l - 1
    if index + 1 < K:
        if A[index] + 1 <= N and A[index] + 1 != A[index + 1]:
            A[index] += 1
    else:
        if A[index] + 1 <= N:
            A[index] += 1

print(*A)