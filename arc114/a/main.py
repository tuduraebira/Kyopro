from math import gcd


N = int(input())
X = list(map(int, input().split()))

p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ans = 10 ** 30

for i in range(2 ** len(p)):
    c = 1
    for j in range(len(p)):
        if (i >> j) & 1:
            c *= p[j]

    for j in range(N):
        if gcd(c, X[j]) == 1:
            break
    else:
        ans = min(ans, c)

print(ans)