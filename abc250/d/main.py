from bisect import bisect_left, bisect_right
import math

N = int(input())

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

# 素数の列挙
prime_bool = sieve_of_eratosthenes(10 ** 6)
prime = []
prime3 = []
for p in range(10 ** 6 + 1):
    if prime_bool[p]:
        prime.append(p)
        prime3.append(p * p * p)

ans = 0
pos = bisect_left(prime3, N)
#print(pos)
for i in range(1, pos):
    n = N // prime3[i]
    ans += min(bisect_right(prime, n), i)

print(ans)