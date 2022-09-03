from collections import deque


S = input()
K = int(input())

que = deque()
rem = K
ans = 0
score = 0

for char in S:
    score += 1
    if char == '.':
        que.append(1)
        rem -= 1
    else:
        que.append(0)

    while rem < 0:
        rem += que.popleft()
        score -= 1

    ans = max(ans, score)

print(ans)