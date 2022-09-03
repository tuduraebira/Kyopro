MOD = 998244353

def g(x):
    return x * (x + 1) // 2

N = int(input())
L = len(str(N))

ans = 0
for i in range(1, L + 1):
    k = min(N, 10 ** i - 1) - (10 ** (i - 1) - 1)
    ans += g(k)
    ans %= MOD

print(ans)