N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    ans = []  # 文字列の連結が遅いPyPyでは、文字列を+=で連結するとTLEになります
    for j in range(R, S + 1):
        if (i - j == A - B) or (i + j == A + B):
            ans.append("#")
        else:
            ans.append(".")
    print(*ans, sep="")