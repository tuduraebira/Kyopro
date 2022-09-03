N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = [0 for i in range(N)]
Q[0] = A[0]
for i in range(1, N):
    Q[i] = A[i] - A[i - 1]

ans = 1
for i in range(N):
    ans *= (Q[i] + 1)
    ans %= 10 ** 9 + 7

print(ans)