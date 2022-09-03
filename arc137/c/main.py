from math import gcd


L, R = map(int, input().split())
for i in reversed(range(R - L + 1)):
    for j in range(L, R - i + 1):
        if gcd(i, j) == 1:
            print(i)
            exit()