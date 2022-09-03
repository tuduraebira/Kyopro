N = int(input())
T = []
K = []
A = []
for _ in range(N):
    t, k, *a = map(int, input().split())
    T.append(t)
    K.append(k)
    A.append(a)

waza = [A[-1]]
waza_s = [False] * N
ans = T[-1]
while len(waza) != 0:
    tmp = []

    for w_l in waza:
        for w in w_l:
            if waza_s[w - 1] == False:
                waza_s[w - 1] = True
                ans += T[w - 1]
                tmp.append(A[w - 1])
    
    waza = tmp

print(ans)