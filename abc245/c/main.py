N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [False] * (N + 1)
ep = [False] * (N + 1)

dp[1] = True
ep[1] = True

for i in range(2, N + 1):
    if dp[i - 1]:
        if abs(A[i - 1] - A[i - 2]) <= K:
            dp[i] = True
        if abs(B[i - 1] - A[i - 2]) <= K:
            ep[i] = True
    
    if ep[i - 1]:
        if abs(A[i - 1] - B[i - 2]) <= K:
            dp[i] = True
        if abs(B[i - 1] - B[i - 2]) <= K:
            ep[i] = True
    #print(dp, ep)

if dp[-1] or ep[-1]:
    print("Yes")
else:
    print("No")