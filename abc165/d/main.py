from math import floor


A, B, N = map(int, input().split())

def calc(x):
    return floor((A * x) / B) - A * floor(x / B)

if N < B:
    print(calc(N))
else:
    print(calc(B - 1))