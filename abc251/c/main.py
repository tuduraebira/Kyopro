N = int(input())
v = {}
ma = -1
ans = 0
for i in range(N):
    S, T = map(str, input().split())
    #print(S, T)
    if v.get(S) == None:
        v[S] = True
        if ma < int(T):
            ma = int(T)
            ans = i + 1

print(ans)