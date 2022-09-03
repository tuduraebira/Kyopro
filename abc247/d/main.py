from collections import deque


Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

tutu = deque()
for q in query:
    if q[0] == 1:
        tutu.append([q[1], q[2]])
    else:
        c = q[1]
        ans = 0
        
        while tutu[0][1] < c:
            c -= tutu[0][1]
            ans += tutu[0][0] * tutu[0][1]
            tutu.popleft()
        
        tutu[0][1] -= c
        ans += c * tutu[0][0]
        if tutu[0][1] == 0:
            tutu.popleft()
        
        print(ans)