N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ABs = sorted(AB, key=lambda x: x[1])

t = 0
for a, b in ABs:
    t += a
    if t > b:
        print("No")
        exit()

print("Yes")