mod = 10 ** 9 + 7

N = int(input())

ans = pow(10, N, mod)
ans -= pow(9, N, mod) * 2
ans += pow(8, N, mod)
print(ans % mod)