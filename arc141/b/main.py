N,M = map(int,input().split())
MOD = 998244353
K = len(bin(M))-2
print(K)

P = [pow(2,i,MOD) for i in range(K)]
print(P)
P[-1] = (M - sum(P[:-1])) % MOD
print(P)

dp = P[:]
for _ in range(min(61, N-1)):
    dp2 = [0] * K
    for i in range(K-1):
        for j in range(i+1,K):
            dp2[j] += dp[i] * P[j]
            dp2[j] %= MOD
    print(dp2)
    dp = dp2

print(sum(dp) % MOD)
