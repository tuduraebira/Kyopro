N = int(input())
A = [input() for _ in range(N)]

dire = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

ans = -1
for i in range(N):
    for j in range(N):
        for d in dire:
            num = A[i][j]
            for _ in range(N - 1):
                i += d[1]
                j += d[0]
                if i < 0:
                    i = N - 1
                if i >= N:
                    i = 0
                if j < 0:
                    j = N - 1
                if j >= N:
                    j = 0
                num += A[i][j]
            ans = max(ans, int(num))

print(ans)