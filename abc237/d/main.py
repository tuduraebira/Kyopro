from collections import deque


N = int(input())
S = input()

d = deque()
d.append(N)
for i, c in enumerate(reversed(S)):
    if c == 'L':
        d.append((N - 1) - i)
    else:
        d.appendleft((N - 1) - i)

print(*d)