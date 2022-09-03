from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)

N, M = map(int, input().split())
S = input()
T = input()

ch = {}
L = lcm(len(S), len(T))
for i, s in enumerate(S):
    X = i * (L / N) + 1
    ch[X] = s

for i, t in enumerate(T):
    X = i * (L / M) + 1
    if ch.get(X) != None:
        if ch[X] != t:
            print(-1)
            exit()

print(L)