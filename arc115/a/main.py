N, M = map(int, input().split())
S = [input() for _ in range(N)]

guu = 0
ki = 0
for s in S:
    one = 0
    zero = 0
    for c in s:
        if c == '0':
            zero += 1
        else:
            one += 1

    if one % 2 == 0:
        guu += 1
    else:
        ki += 1

print(guu * ki)