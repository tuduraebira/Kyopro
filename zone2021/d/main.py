from collections import deque


S = input()

rev = False
deq = deque()
for s in S:
    if s == 'R':
        rev = not rev
    else:
        if rev:
            deq.appendleft(s)
        else:
            deq.append(s)

if rev:
    deq.reverse()

ans = []
for c in deq:
    if len(ans) > 0 and ans[-1] == c:
        ans.pop()
    else:
        ans.append(c)

print(''.join(ans))