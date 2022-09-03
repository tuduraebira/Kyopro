from math import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

N, A, B = map(int, input().split())

sumN = (N + 1) * N // 2

sumA = A * ((N // A + 1) * (N // A) // 2)
sumB = B * ((N // B + 1) * (N // B) // 2)
lcmAB = lcm(A, B)
sumAB = lcmAB * ((N // lcmAB + 1) * (N // lcmAB) // 2)

print(sumN - sumA - sumB + sumAB)  