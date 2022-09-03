N = int(input())

def f(a, b):
    return (a*a*a + a*a*b + a*b*b + b*b*b)

ans = 10 ** 31
j = 1000000
for i in range(1000001):
    while f(i, j) >= N and j >= 0:
        ans = min(ans, f(i, j))
        j -= 1

print(ans)