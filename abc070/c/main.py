from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

N = int(input())

ans = 1
for _ in range(N):
    T = int(input())
    ans = lcm(ans, T)

print(ans)