N = int(input())
a = list(map(int, input().split()))
S = [[-1, 0]]
ans = 0

for i in a:
    j, cnt = S[-1]
    ans += 1

    if i == j:
        S[-1][1] += 1
    else:
        S.append([i, 1])
    
    if S[-1][0] == S[-1][1]:
        S.pop()
        ans -= i

    print(ans)