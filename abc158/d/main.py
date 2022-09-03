from collections import deque


S = input()
Q = int(input())
query = [list(map(str, input().split())) for _ in range(Q)]

deq = deque(S)
is_rev = False

for q in query:
    if q[0] == '1':
        is_rev = not is_rev
    else:
        if q[1] == '1':
            if is_rev:
                deq.append(q[2])
            else:
                deq.appendleft(q[2])
        else:
            if is_rev:
                deq.appendleft(q[2])
            else:
                deq.append(q[2])

if is_rev:
    print(''.join(reversed(deq)))
else:
    print(''.join(deq))