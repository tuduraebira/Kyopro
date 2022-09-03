N = int(input())
P = list(map(int, input().split()))

ans = 0
index = N
while True:
    ans += 1
    index = P[index - 2]

    if index == 1:
        break

print(ans)