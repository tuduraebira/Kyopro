N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

pt = 0
ans = []
for s in S:
    if s == T[pt]:
        ans.append("Yes")
        pt += 1
    else:
        ans.append("No")

for yn in ans:
    print(yn)