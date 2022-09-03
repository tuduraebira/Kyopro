N = int(input())
mod = 998244353

def comb(n,k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

kaijou = [1]
k = 1
for i in range(1, 25001):
    k *= i
    k %= mod
    kaijou.append(k)

no = 0
for i in range(N, N * N - N + 2):
    n = i - 1
    k = N - 1
    r = N * N - i
    rest = N * N - (2 * k + 1)
    o = (N * N) * comb(n, k) * kaijou[k] * comb(r, k) * kaijou[k] * kaijou[rest]
    #print(comb(r, k))
    o %= mod
    no += o
    no %= mod

ans = kaijou[N * N] - no
ans %= mod
print(ans)
