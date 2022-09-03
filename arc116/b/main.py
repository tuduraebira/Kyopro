N = int(input())
A = list(map(int, input().split()))
mod = 998244353

A.sort(reverse=True)

ans = 0
S = 0
for a in A:
    ans += a * a
ans %= mod

for i in range(1, N):
    ans += (A[i] * (2 * S + A[i - 1]))
    ans %= mod
    S = 2 * S + A[i - 1]
    S %= mod

print(ans % mod)