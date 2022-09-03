N = int(input())
T = list(map(int, input().split()))

ans = 0
for i in range(N):
    n = ans >> T[i]
    if n:
        if n & 1:
            n += 2
        else:
            n += 1
    else:
        n += 1

    ans = n << T[i]

print(ans)