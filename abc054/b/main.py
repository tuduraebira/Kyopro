N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for ai in range(N - M + 1):
    for aj in range(N - M + 1):
        isMatch = False
        for bi in range(M):
            for bj in range(M):
                if A[ai + bi][aj + bj] == B[bi][bj]:
                    isMatch = True
                else:
                    isMatch = False
                    break

                if isMatch and bi == M - 1 and bj == M - 1:
                    print('Yes')
                    exit()
            if not isMatch:
                break
        if not isMatch:
            continue
print('No')
