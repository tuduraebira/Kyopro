from collections import deque


n = int(input())
a = list(map(int, input().split()))

d = deque()
if len(a) % 2 == 0:
    for i, an in enumerate(a):
        if i % 2 == 0:
            d.append(an)
        else:
            d.appendleft(an)
else:
    for i, an in enumerate(a):
        if i % 2 == 0:
            d.appendleft(an)
        else:
            d.append(an)

print(*d)