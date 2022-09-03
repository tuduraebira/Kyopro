N = int(input())
A = list(map(int, input().split()))

erase = A[-1]
for i in range(N - 1):
    if A[i] > A[i + 1]:
        erase = A[i]
        break

ans = []
for a in A:
    if a != erase:
        ans.append(a)

print(*ans)