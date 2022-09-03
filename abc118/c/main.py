from math import gcd


N = int(input())
A = list(map(int, input().split()))

def lcm(a, b):
    return (a * b) // gcd(a, b)

gcd_num = A[0]
for i in range(N - 1):
    gcd_num = gcd(gcd_num, A[i + 1])

print(gcd_num)