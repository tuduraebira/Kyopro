from math import gcd


A, B, C, D = map(int, input().split())

def num(x):
    g = gcd(C, D)
    l = C // g * D
    return x - x//C - x//D + x//l

print(int(num(B) - num(A-1)))