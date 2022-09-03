S = input()
K = int(input())
N = len(S)

A = [[S[0], 1]]
for i in range(1, N):
    if S[i] == A[-1][0]:
        A[-1][1] += 1
    else:
        A.append([S[i], 1])

ans = 0

if len(A) == 1:
    ans = N * K // 2
else:
    for a in A:
        ans += a[1] // 2
    ans *= K
    if (A[0][0] == A[-1][0]) and (A[0][1] % 2 == 1 and A[-1][1] % 2 == 1):
        ans += (K - 1)

print(ans)