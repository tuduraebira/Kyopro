from collections import deque

N = int(input())
slot = []
for _ in range(N):
    S = input()
    slot.append(S)

ans = 10 ** 10
for i in range(10):
    dic = {}
    a = 0

    for s in slot:
        for j, c in enumerate(s):
            if i == int(c):
                if dic.get(j) == None:
                    a = max(a, j)
                    dic[j] = 1
                else:
                    a = max(a, j + dic[j] * 10)
                    dic[j] += 1

    ans = min(ans, a)

print(ans)